"""
FILE MENTAHAN: app.py
TUGAS SPRINT: Implementasikan kelas MenuTrie untuk fitur Search!
"""
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from data_structures import CustomQueue, PendingMap, UndoStack

app = Flask(__name__)

# ==========================================
# TUGAS 4: STRUKTUR DATA TRIE (Prefix Tree)
# ==========================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.menu_key = None

class MenuTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, menu_key):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.menu_key = menu_key

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return [] 
            node = node.children[char]
        
        results = set()
        self._dfs(node, results)
        return list(results)

    def _dfs(self, node, results):
        if node.is_end:
            results.add(node.menu_key)
        for child in node.children.values():
            self._dfs(child, results)

# ==========================================
# STATE MEMORI (Instansiasi Objek SDA)
# ==========================================
main_queue = CustomQueue()   
pending_map = PendingMap()      
undo_stack = UndoStack()        
order_history = []            
order_counter = 1
cart = {} 
customer_info = {"nama": "", "meja": "11"}

MENU_DB = {
    "Fries": {"nama": "Classic Salted Fries", "varian": "Large", "harga": 4.5, "img": "🍟"},
    "Macchiato": {"nama": "Caramel Macchiato", "varian": "No Sugar", "harga": 5.5, "img": "🥤"},
    "Chicken": {"nama": "Fried Chicken Blast", "varian": "Big", "harga": 15.0, "img": "🍗"},
    "Pasta": {"nama": "Pasta Bolognese", "varian": "Extra Spicy", "harga": 12.0, "img": "🍝"},
    "Steak": {"nama": "Grilled Steak", "varian": "Medium Rare", "harga": 20.0, "img": "🥩"},
    "Salad": {"nama": "Fresh Salad", "varian": "Sesame Dressing", "harga": 8.0, "img": "🥗"},
    "Matcha": {"nama": "Premium Matcha Latte", "varian": "Iced, Less Sugar", "harga": 6.5, "img": "🍵"},
    "Croissant": {"nama": "Butter Croissant", "varian": "Warm & Flaky", "harga": 3.5, "img": "🥐"},
    "Tiramisu": {"nama": "Classic Tiramisu", "varian": "Espresso Soaked", "harga": 6.0, "img": "🍰"},
    "Cheesecake": {"nama": "Strawberry Cheesecake", "varian": "New York Style", "harga": 7.0, "img": "🍰"},
    "Sandwich": {"nama": "Club Sandwich", "varian": "Smoked Beef", "harga": 8.5, "img": "🥪"},
    "LemonTea": {"nama": "Iced Lemon Tea", "varian": "Regular", "harga": 3.0, "img": "🍹"},
    "Burger": {"nama": "Smash Burger", "varian": "Double Beef", "harga": 9.5, "img": "🍔"},
    "Espresso": {"nama": "Espresso Shot", "varian": "Double Ristretto", "harga": 3.0, "img": "☕"},
    "Pancake": {"nama": "Chocolate Pancake", "varian": "Maple Syrup", "harga": 5.0, "img": "🥞"}
}

menu_trie = MenuTrie()
for key, item in MENU_DB.items():
    full_name = item['nama']
    menu_trie.insert(full_name, key)
    words = full_name.split()
    if len(words) > 1:
        for i in range(1, len(words)):
            menu_trie.insert(" ".join(words[i:]), key)

def current_time():
    return datetime.now().strftime("%H:%M")

@app.route('/')
def home():
    raw_mode = request.args.get('mode', 'cashier').lower()
    mode = 'cashier' if raw_mode == 'kasir' else raw_mode
    if mode not in ['cashier', 'barista']: mode = 'cashier'
        
    tab = request.args.get('tab', 'menu')
    q = request.args.get('q', '')
    if str(q).lower() == 'none': q = ''
    q = q.strip()
    
    filtered_menu = MENU_DB
    if q and tab == 'menu' and mode == 'cashier':
        found_keys = menu_trie.search_prefix(q)
        if found_keys: # Mencegah error jika tim belum mengimplementasikan Trie
            filtered_menu = {k: MENU_DB[k] for k in found_keys if k in MENU_DB}
        else:
            filtered_menu = {}
            
    latest_history = list(reversed(order_history))
    if q and tab == 'history':
        q_lower = q.lower()
        latest_history = [
            h for h in latest_history 
            if q_lower in h['nama_pelanggan'].lower() or q_lower in h['nomor']
        ]
    
    subtotal_cart = sum(item['harga'] * item['qty'] for item in cart.values())
    service_fee = 1.0 if subtotal_cart > 0 else 0
    discount = -1.5 if subtotal_cart > 20 else 0
    total_cart = subtotal_cart + service_fee + discount if subtotal_cart > 0 else 0

    return render_template(
        'index.html', mode=mode, tab=tab, menu_db=filtered_menu, cart=cart, customer=customer_info,
        cart_count=sum(item['qty'] for item in cart.values()), subtotal_c=f"{subtotal_cart:.1f}",
        service_c=f"{service_fee:.1f}", discount_c=f"{discount:.1f}", total_c=f"{total_cart:.1f}",
        orders=main_queue.display(), pending=pending_map.get_all(), history=latest_history,
        queue_size=main_queue.size(), pending_size=pending_map.size(), undo_size=undo_stack.size()
    )

@app.route('/cart/add/<item_id>', methods=['POST'])
def cart_add(item_id):
    if item_id in MENU_DB:
        if item_id in cart: cart[item_id]['qty'] += 1
        else: cart[item_id] = MENU_DB[item_id].copy(); cart[item_id]['qty'] = 1
    q_param = request.form.get('q', '')
    if str(q_param).lower() == 'none': q_param = ''
    return redirect(url_for('home', mode='cashier', tab='menu', q=q_param))

@app.route('/cart/min/<item_id>', methods=['POST'])
def cart_min(item_id):
    if item_id in cart:
        cart[item_id]['qty'] -= 1
        if cart[item_id]['qty'] <= 0: del cart[item_id]
    q_param = request.form.get('q', '')
    if str(q_param).lower() == 'none': q_param = ''
    return redirect(url_for('home', mode='cashier', tab='menu', q=q_param))

@app.route('/cart/clear', methods=['POST'])
def cart_clear():
    cart.clear()
    return redirect(url_for('home', mode='cashier', tab='menu'))

@app.route('/cart/checkout', methods=['POST'])
def cart_checkout():
    global order_counter
    raw_name = request.form.get('customer_name', '').strip()
    nama = raw_name if raw_name else f'Cust #{order_counter}'
    meja = request.form.get('table_no', '11')
    
    if cart:
        new_order = {
            "id": "ORD-" + uuid.uuid4().hex[:6].upper(), "nomor": f"{order_counter:03}",
            "nama_pelanggan": nama, "meja": meja, "items": list(cart.values()),
            "waktu": current_time(), "total": sum(i['harga'] * i['qty'] for i in cart.values())
        }
        main_queue.enqueue(new_order)
        undo_stack.push(new_order)
        order_counter += 1
        cart.clear()
    return redirect(url_for('home', mode='cashier', tab='menu'))

@app.route('/cashier/undo_kitchen', methods=['POST'])
def cashier_undo_kitchen():
    global main_queue 
    if not undo_stack.is_empty():
        canceled_order = undo_stack.pop()
        current_items = main_queue.display()
        main_queue = CustomQueue() 
        is_removed = False
        for item in current_items:
            if item["id"] == canceled_order["id"] and not is_removed:
                is_removed = True
                continue
            main_queue.enqueue(item)
    return redirect(url_for('home', mode='cashier', tab='menu'))

@app.route('/barista/process', methods=['POST'])
def barista_process():
    if not main_queue.is_empty():
        completed = main_queue.dequeue() 
        if completed: # Mencegah error jika dequeue belum diimplementasi tim
            completed['status'] = 'Completed'
            completed['waktu_selesai'] = current_time()
            completed['nama_ringkas'] = completed['items'][0]['nama'] + (" etc." if len(completed['items']) > 1 else "")
            order_history.append(completed)
    return redirect(url_for('home', mode='barista', tab='menu'))

@app.route('/barista/pending', methods=['POST'])
def barista_pending():
    reason = request.form.get('alasan', 'Waiting for ingredients')
    if not main_queue.is_empty():
        held_order = main_queue.dequeue()
        if held_order:
            held_order['alasan'] = reason
            pending_map.add(held_order['id'], held_order) 
    return redirect(url_for('home', mode='barista', tab='menu'))

@app.route('/barista/resolve_pending/<order_id>', methods=['POST'])
def barista_resolve_pending(order_id):
    if pending_map.exists(order_id):
        completed = pending_map.remove(order_id)
        if completed:
            completed['status'] = 'Resolved from Pending'
            completed['waktu_selesai'] = current_time()
            completed['nama_ringkas'] = completed['items'][0]['nama'] + (" etc." if len(completed['items']) > 1 else "")
            order_history.append(completed)
    return redirect(url_for('home', mode='barista', tab='pending'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)