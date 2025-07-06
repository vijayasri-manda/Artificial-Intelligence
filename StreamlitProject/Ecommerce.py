# import streamlit as st
# import pandas as pd
#
# # Page config
# st.set_page_config(page_title="🛒 Streamlit E-Commerce", layout="wide")
#
# # Sample Product Data
# products = [
#     {"id": 1, "name": "Smartphone", "price": 25000, "category": "Electronics", "image": "https://via.placeholder.com/150"},
#     {"id": 2, "name": "Laptop", "price": 60000, "category": "Electronics", "image": "https://via.placeholder.com/150"},
#     {"id": 3, "name": "Headphones", "price": 2500, "category": "Accessories", "image": "https://via.placeholder.com/150"},
#     {"id": 4, "name": "Smart Watch", "price": 4500, "category": "Accessories", "image": "https://via.placeholder.com/150"},
#     {"id": 5, "name": "Shoes", "price": 3000, "category": "Fashion", "image": "https://via.placeholder.com/150"},
#     {"id": 6, "name": "T-shirt", "price": 800, "category": "Fashion", "image": "https://via.placeholder.com/150"},
# ]
#
# # Session state for cart
# if 'cart' not in st.session_state:
#     st.session_state.cart = []
#
# # Title
# st.title("🛍️ Streamlit E-Commerce Store")
#
# # Sidebar with Category Filter and Search
# st.sidebar.header("🔍 Filter Products")
# categories = ["All"] + sorted(list(set([p['category'] for p in products])))
# selected_category = st.sidebar.selectbox("Select Category", categories)
# search_term = st.sidebar.text_input("Search Products")
#
# # Filter products by category and search
# def filter_products():
#     filtered = products
#     if selected_category != "All":
#         filtered = [p for p in filtered if p["category"] == selected_category]
#     if search_term:
#         filtered = [p for p in filtered if search_term.lower() in p["name"].lower()]
#     return filtered
#
# # Display products
# st.subheader("🛒 Products")
# cols = st.columns(3)
# filtered_products = filter_products()
#
# if not filtered_products:
#     st.warning("No products found.")
# else:
#     for index, product in enumerate(filtered_products):
#         with cols[index % 3]:
#             st.image(product["image"], width=150)
#             st.write(f"**{product['name']}**")
#             st.write(f"Price: ₹ {product['price']}")
#             quantity = st.number_input(f"Quantity ({product['name']})", min_value=1, max_value=10, value=1, key=f"qty_{product['id']}")
#             if st.button("Add to Cart", key=f"add_{product['id']}"):
#                 item = product.copy()
#                 item['quantity'] = quantity
#                 st.session_state.cart.append(item)
#                 st.success(f"{quantity} {product['name']} added to cart!")
#
# st.markdown("---")
#
# # Cart Section
# st.subheader("🛒 Your Cart")
# if st.session_state.cart:
#     cart_df = pd.DataFrame(st.session_state.cart)
#     cart_df["Total"] = cart_df["price"] * cart_df["quantity"]
#     st.dataframe(cart_df[["name", "price", "quantity", "Total"]])
#
#     total_amount = cart_df["Total"].sum()
#     st.write(f"### 🧾 Total Amount: ₹ {total_amount}")
#
#     if st.button("Clear Cart"):
#         st.session_state.cart.clear()
#         st.success("Cart cleared.")
#
#     st.markdown("---")
#
#     # Checkout Section
#     st.subheader("📦 Checkout")
#     name = st.text_input("Your Name")
#     address = st.text_area("Shipping Address")
#     mobile = st.text_input("Mobile Number")
#
#     if st.button("Place Order"):
#         if not name or not address or not mobile:
#             st.error("Please fill all the details to place the order.")
#         else:
#             st.success(f"Order placed successfully for ₹ {total_amount}!\n\nThank you {name} 🙌")
#             st.session_state.cart.clear()
#
# else:
#     st.write("Your cart is empty.")
#
# st.markdown("---")
# st.write("💡 Demo E-Commerce web app built with Streamlit.")
#
import streamlit as st

# Page config
st.set_page_config(
    page_title="Elegant Ecommerce Store",
    page_icon="🛒",
    layout="wide",
)
# Custom CSS styling for the app to reflect the default design guidelines
custom_css = """
<style>
    /* Typography */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');
    html, body, [class*="st"]  {
        font-family: 'Poppins', sans-serif;
        background-color: #ffffff;
        color: #374151;
    }
    /* Header */
    .header-container {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: white;
        box-shadow: 0 1px 5px rgb(0 0 0 / 0.1);
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .logo {
        font-size: 1.75rem;
        font-weight: 800;
        color: #111827;
        user-select: none;
    }
    .nav-links > a {
        margin-left: 1.5rem;
        font-weight: 600;
        color: #6b7280;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .nav-links > a:hover {
        color: #111827;
    }
    /* Hero */
    .hero-section {
        text-align: center;
        padding: 8rem 2rem 6rem 2rem;
        max-width: 900px;
        margin: 0 auto;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #111827;
        line-height: 1.1;
        margin-bottom: 1rem;
    }
    .hero-subtext {
        font-size: 1.25rem;
        color: #6b7280;
        margin-bottom: 3rem;
        font-weight: 500;
    }
    .cta-button {
        background-color: #111827;
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        font-size: 1.125rem;
        font-weight: 700;
        border-radius: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .cta-button:hover {
        background-color: #374151;
    }
    /* Product Cards */
    .product-card {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgb(0 0 0 / 0.1);
        padding: 1rem;
        background: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: box-shadow 0.3s ease;
        height: 100%;
    }
    .product-card:hover {
        box-shadow: 0 6px 20px rgb(0 0 0 / 0.15);
    }
    .product-image {
        border-radius: 0.75rem;
        object-fit: cover;
        width: 100%;
        height: 180px;
        margin-bottom: 1rem;
    }
    .product-name {
        font-weight: 700;
        font-size: 1.1rem;
        color: #111827;
        margin-bottom: 0.5rem;
        flex-grow: 1;
    }
    .product-price {
        font-weight: 600;
        font-size: 1rem;
        color: #2563eb;
        margin-bottom: 1rem;
    }
    .add-to-cart-btn {
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 0;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        transition: background-color 0.3s ease;
    }
    .add-to-cart-btn:hover {
        background-color: #1d4ed8;
    }
    /* Cart Section */
    .cart-section {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgb(0 0 0 / 0.08);
        padding: 1.5rem;
        background: #fafafa;
        max-width: 400px;
        position: sticky;
        top: 5rem;
        height: fit-content;
    }
    .cart-title {
        font-weight: 700;
        font-size: 1.6rem;
        margin-bottom: 1rem;
        color: #111827;
    }
    .cart-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.8rem;
        font-size: 1rem;
        font-weight: 600;
        color: #4b5563;
    }
    .cart-item-name {
        flex-grow: 1;
        margin-right: 1rem;
    }
    .cart-item-controls button {
        background-color: #2563eb;
        border: none;
        color: white;
        font-weight: 700;
        border-radius: 6px;
        padding: 0 8px;
        margin-left: 0.25rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
        height: 28px;
        line-height: 24px;
    }
    .cart-item-controls button:hover {
        background-color: #1d4ed8;
    }
    .cart-total {
        font-weight: 800;
        font-size: 1.25rem;
        margin-top: 1rem;
        color: #111827;
    }
    .empty-cart {
        font-style: italic;
        color: #9ca3af;
        margin-top: 1rem;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Sample products
products = [
    {
        "id": 1,
        "name": "Elegant Leather Backpack",
        "price": 129.99,
        "image": "https://images.unsplash.com/photo-1515191107209-c28698631303?auto=format&fit=crop&w=500&q=80",
    },
    {
        "id": 2,
        "name": "Classic Wristwatch",
        "price": 199.0,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80",
    },
    {
        "id": 3,
        "name": "Stylish Sunglasses",
        "price": 89.5,
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=500&q=80",
    },
    {
        "id": 4,
        "name": "Modern Sneakers",
        "price": 150.0,
        "image": "https://images.unsplash.com/photo-1507668077129-56b9be92e468?auto=format&fit=crop&w=500&q=80",
    },
    {
        "id": 5,
        "name": "Cozy Knit Sweater",
        "price": 75.0,
        "image": "https://images.unsplash.com/photo-1521334884684-d80222895322?auto=format&fit=crop&w=500&q=80",
    },
    {
        "id": 6,
        "name": "Luxury Headphones",
        "price": 299.99,
        "image": "https://images.unsplash.com/photo-1518441902118-259d2cc3feae?auto=format&fit=crop&w=500&q=80",
    },
]

# Header with logo and nav
st.markdown("""
<div class="header-container">
    <div class="logo">EcomShop</div>
    <nav class="nav-links">
        <a href="#products">Products</a>
        <a href="#cart">Cart</a>
    </nav>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<section class="hero-section">
    <h1 class="hero-title">Shop the finest products with elegance</h1>
    <p class="hero-subtext">Curated selection of stylish essentials for your lifestyle.</p>
    <button class="cta-button" onclick="window.location='#products'">Browse Products</button>
</section>
""", unsafe_allow_html=True)

# Products Section
st.markdown('<div id="products"></div>', unsafe_allow_html=True)
st.subheader("Products")
cols = st.columns(3, gap="medium")

for idx, product in enumerate(products):
    col = cols[idx % 3]
    with col:
        st.markdown(
            f"""
            <div class="product-card">
                <img src="{product['image']}" alt="{product['name']}" class="product-image"/>
                <div class="product-name">{product['name']}</div>
                <div class="product-price">${product['price']:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Add to Cart", key=f"add_{product['id']}"):
            cart = st.session_state.cart
            if product['id'] in cart:
                cart[product['id']]['quantity'] += 1
            else:
                cart[product['id']] = {
                    "name": product['name'],
                    "price": product['price'],
                    "quantity": 1,
                }
            st.experimental_rerun()

# Cart Section on the right side
st.markdown('<div id="cart"></div>', unsafe_allow_html=True)
st.markdown("---")
cart_items = st.session_state.cart

st.markdown('<div class="cart-section">', unsafe_allow_html=True)
st.markdown('<div class="cart-title">Shopping Cart</div>', unsafe_allow_html=True)

if len(cart_items) == 0:
    st.markdown('<div class="empty-cart">Your cart is empty.</div>', unsafe_allow_html=True)
else:
    total = 0.0
    for pid, item in cart_items.items():
        subtotal = item['price'] * item['quantity']
        total += subtotal
        st.markdown(
            '<div class="cart-item">',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="cart-item-name">{item["name"]} x {item["quantity"]} = ${subtotal:.2f}</div>',
            unsafe_allow_html=True,
        )
        # Quantity controls
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("-", key=f"minus_{pid}"):
                if item['quantity'] > 1:
                    cart_items[pid]['quantity'] -= 1
                else:
                    del cart_items[pid]
                st.experimental_rerun()
        with col2:
            if st.button("+", key=f"plus_{pid}"):
                cart_items[pid]['quantity'] += 1
                st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="cart-total">Total: ${total:.2f}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

