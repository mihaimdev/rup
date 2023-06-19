import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

st.set_page_config(page_icon="✂️", page_title="RUP",
                   initial_sidebar_state="collapsed",
                   layout="wide")
st.sidebar.title("COPSI RUP")
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data("rup1.csv")
#st.dataframe(df)

#st.button("Rerun")
#filtered_df = df = pd.read_csv("rup1.csv",dtype=str).fillna("")
st.title("Registrul Unic al Psihologilor")
shows = df

from st_aggrid import GridUpdateMode, DataReturnMode

gb = GridOptionsBuilder.from_dataframe(shows)
# enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
# gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
gridOptions = gb.build()

# st.success(
#     f"""
#         💡 Tip! Hold the shift key when selecting rows to select multiple rows at once!
#         """
# )
with st.spinner("Lista se încarcă...mai greu la încrput :) "):
    response = AgGrid(
        shows,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
    )

    df = pd.DataFrame(response["selected_rows"])
