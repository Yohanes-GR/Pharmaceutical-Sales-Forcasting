import user_overview_page
import promotion_page

import streamlit as st

PAGES = {
     "Data Overview": user_overview_page,
     "Promotion Effect on Stores": promotion_page
}

selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
