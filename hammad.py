import streamlit as st

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Luxora Grand Hotel",
    page_icon="🏨",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #07111f, #12233a);
    color: white;
}

.main-title {
    font-size: 55px;
    font-weight: bold;
    color: #e7c46a;
    text-align: center;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #c7d0dc;
    font-size: 20px;
    margin-bottom: 30px;
}

.card {
    background: #17283e;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid #2d405a;
}

.room-card {
    background: #17283e;
    padding: 15px;
    border-radius: 18px;
    margin-bottom: 15px;
    border: 1px solid #30445e;
}

.price {
    color: #e7c46a;
    font-size: 22px;
    font-weight: bold;
}

.available {
    color: #43d17b;
    font-weight: bold;
}

.occupied {
    color: #ff7373;
    font-weight: bold;
}

h2, h3 {
    color: #e7c46a;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================

rooms = []

for i in range(1, 16):

    if i <= 8:
        room_type = "Deluxe Room"
        price = 14500
    else:
        room_type = "Executive Suite"
        price = 22000

    rooms.append({
        "number": i,
        "type": room_type,
        "price": price,
        "status": "Available"
    })


tables = []

for i in range(1, 13):

    tables.append({
        "number": i,
        "status": "Available"
    })


menu = [
    {
        "name": "Chicken Biryani",
        "category": "Main Course",
        "price": 850,
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
    },
    {
        "name": "Mutton Karahi",
        "category": "Main Course",
        "price": 1850,
        "image": "https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7"
    },
    {
        "name": "Chicken Handi",
        "category": "Main Course",
        "price": 1450,
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398"
    },
    {
        "name": "Beef Steak",
        "category": "BBQ",
        "price": 2400,
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d"
    },
    {
        "name": "Chicken Seekh Kebab",
        "category": "BBQ",
        "price": 1100,
        "image": "https://images.unsplash.com/photo-1599487488170-d11ec9c172f0"
    },
    {
        "name": "Grilled Chicken",
        "category": "Healthy",
        "price": 1250,
        "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435"
    },
    {
        "name": "Chicken Shawarma",
        "category": "Fast Food",
        "price": 650,
        "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783"
    },
    {
        "name": "French Fries",
        "category": "Sides",
        "price": 450,
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"
    },
    {
        "name": "Fresh Salad",
        "category": "Sides",
        "price": 400,
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd"
    },
    {
        "name": "Chocolate Cake",
        "category": "Dessert",
        "price": 650,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    },
    {
        "name": "Gulab Jamun",
        "category": "Dessert",
        "price": 450,
        "image": "https://images.unsplash.com/photo-1666190094765-4b9b1b1c1e0f"
    },
    {
        "name": "Kunafa",
        "category": "Dessert",
        "price": 750,
        "image": "https://images.unsplash.com/photo-1579888944880-d98341245702"
    },
    {
        "name": "Ice Cream",
        "category": "Dessert",
        "price": 400,
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
    },
    {
        "name": "Mango Lassi",
        "category": "Drinks",
        "price": 350,
        "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888"
    },
    {
        "name": "Fresh Lime",
        "category": "Drinks",
        "price": 300,
        "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd"
    }
]

# =========================
# SESSION STATE
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "selected_table" not in st.session_state:
    st.session_state.selected_table = 1

if "page" not in st.session_state:
    st.session_state.page = "Home"

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">✦ LUXORA GRAND</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Luxury Hotel • Halal Restaurant • Professional POS</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🏨 LUXORA GRAND")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Hotel Rooms",
        "Restaurant POS",
        "Menu & Prices",
        "Reservations"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 HOTEL OPEN")
st.sidebar.success("🟢 HALAL RESTAURANT")

# =========================
# HOME
# =========================

if page == "Home":

    st.image(
        "https://images.unsplash.com/photo-1566073771259-6a8506099945",
        use_container_width=True
    )

    st.markdown(
        "<h2 style='text-align:center;'>A Cinematic Stay. A Memorable Table.</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🏨 Rooms", "15")

    with col2:
        st.metric("🍽️ Tables", "12")

    with col3:
        st.metric("🥘 Menu Items", "15")

    with col4:
        st.metric("☪️ Halal", "100%")

    st.markdown("---")

    st.info(
        "Welcome to Luxora Grand Hotel & Restaurant. "
        "Enjoy comfortable rooms, halal food, desserts and fair prices."
    )

# =========================
# HOTEL ROOMS
# =========================

elif page == "Hotel Rooms":

    st.header("🏨 Hotel Rooms")

    st.write(
        "15 rooms are available in two luxury categories."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            "https://images.unsplash.com/photo-1611892440504-42a792e87d3f",
            use_container_width=True
        )

        st.subheader("Deluxe Room")

        st.write("Elegant room with comfortable bed and premium facilities.")

        st.markdown(
            '<p class="price">Rs 14,500 / Night</p>',
            unsafe_allow_html=True
        )

    with col2:

        st.image(
            "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b",
            use_container_width=True
        )

        st.subheader("Executive Suite")

        st.write("Large luxury suite with premium accommodation.")

        st.markdown(
            '<p class="price">Rs 22,000 / Night</p>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Available Rooms")

    for room in rooms:

        col1, col2, col3, col4 = st.columns(
            [1, 3, 2, 1]
        )

        with col1:
            st.write(f"### {room['number']}")

        with col2:
            st.write(room["type"])

        with col3:
            st.write(f"Rs {room['price']:,}")

        with col4:

            if room["status"] == "Available":

                if st.button(
                    "Reserve",
                    key=f"room_{room['number']}"
                ):

                    room["status"] = "Reserved"

                    st.success(
                        f"Room {room['number']} reserved!"
                    )

# =========================
# RESTAURANT POS
# =========================

elif page == "Restaurant POS":

    st.header("🍽️ Restaurant POS")

    st.subheader("Select Restaurant Table")

    table_cols = st.columns(6)

    for index, table in enumerate(tables):

        with table_cols[index % 6]:

            if table["status"] == "Available":

                if st.button(
                    f"Table {table['number']}\n🟢",
                    key=f"table_{table['number']}"
                ):

                    st.session_state.selected_table = table["number"]

            else:

                st.button(
                    f"Table {table['number']}\n🔴",
                    disabled=True,
                    key=f"busy_{table['number']}"
                )

    st.info(
        f"Selected Table: {st.session_state.selected_table}"
    )

    st.markdown("---")

    st.subheader("🥘 Halal Menu")

    for index, item in enumerate(menu):

        col1, col2, col3 = st.columns(
            [2, 3, 1]
        )

        with col1:

            st.image(
                item["image"],
                width=170
            )

        with col2:

            st.subheader(item["name"])

            st.write(
                f"{item['category']} • ☪️ HALAL"
            )

            st.markdown(
                f'<p class="price">Rs {item["price"]:,}</p>',
                unsafe_allow_html=True
            )

        with col3:

            if st.button(
                "ADD",
                key=f"add_{index}"
            ):

                st.session_state.cart.append(
                    item
                )

                st.success("Added!")

    st.markdown("---")

    st.subheader(
        f"🧾 Order — Table {st.session_state.selected_table}"
    )

    total = 0

    if len(st.session_state.cart) == 0:

        st.info("No items added yet.")

    else:

        for item in st.session_state.cart:

            st.write(
                f"• {item['name']} — Rs {item['price']:,}"
            )

            total += item["price"]

        tax = round(total * 0.05)

        grand_total = total + tax

        st.markdown("---")

        st.write(f"Subtotal: Rs {total:,}")

        st.write(f"Service/Tax 5%: Rs {tax:,}")

        st.markdown(
            f"### 💰 Grand Total: Rs {grand_total:,}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("🧾 Generate Bill"):

                st.success(
                    f"Bill generated successfully!\n"
                    f"Grand Total: Rs {grand_total:,}"
                )

        with col2:

            if st.button("🗑️ Clear Order"):

                st.session_state.cart = []

                st.rerun()

# =========================
# MENU
# =========================

elif page == "Menu & Prices":

    st.header("☪️ Halal Menu & Fair Prices")

    for item in menu:

        col1, col2, col3 = st.columns(
            [2, 4, 1]
        )

        with col1:

            st.image(
                item["image"],
                width=160
            )

        with col2:

            st.subheader(item["name"])

            st.write(
                f"{item['category']} • ☪️ HALAL"
            )

        with col3:

            st.markdown(
                f'<p class="price">Rs {item["price"]:,}</p>',
                unsafe_allow_html=True
            )

        st.markdown("---")

# =========================
# RESERVATIONS
# =========================

elif page == "Reservations":

    st.header("📋 Hotel Reservations")

    for room in rooms:

        if room["status"] == "Available":

            status = "🟢 Available"

        else:

            status = "🔴 Reserved"

        st.markdown(
            f"""
            <div class="room-card">
            <h3>Room {room['number']} — {room['type']}</h3>
            <p>Price: Rs {room['price']:,} / Night</p>
            <p>{status}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown(
    """
    <center>
    <p style="color:#AAB5C5;">
    ✦ LUXORA GRAND HOTEL & RESTAURANT ✦<br>
    Luxury • Comfort • Halal Dining • Fair Prices
    </p>
    </center>
    """,
    unsafe_allow_html=True
)