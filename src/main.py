"""This gives stock info."""
import tkinter
from tkinter import ttk, messagebox
from stocks_api import get_stocks
from create_df import create_df

root = tkinter.Tk()
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.title("Stock Grabber")

# Functions
def get_user_stocks():
    """This gets user stocks from an api and formats them into a dataframe."""
    users_stocks = search_bar.get()
    users_stocks = users_stocks.replace(" ", ", ")
    stock_values = get_stocks(users_stocks)
    try:
        stock_df = create_df(stock_values)
    except KeyError:
        messagebox.showwarning(
            title="Input Error",
            message="The program is unable to recognize a ticker symbol.\n Please try again.",
        )

    # This bit adds the info into our tree block from the dataframe
    tv1["column"] = list(stock_df.columns)
    tv1["show"] = "headings"

    for column in tv1["column"]:
        tv1.heading(column, text=column)

    stock_df_rows = stock_df.to_numpy().tolist()
    for row in stock_df_rows:
        tv1.insert("", "end", values=row)


def clear_data():
    """This deletes instances"""
    tv1.delete(*tv1.get_children())


# Top Frame for viewing stock data
viewing_frame = tkinter.LabelFrame(root, text="Stock Data")
viewing_frame.place(relheight=0.5, relwidth=1)

# Frame for search functions
search_frame = tkinter.LabelFrame(root)
search_frame.place(relheight=1, relwidth=1, rely=0.65, relx=0)

# Search Bar
search_bar = tkinter.Entry(search_frame)
search_bar.place(rely=0.15, relx=0.5, relwidth=0.75, relheight=0.05, anchor="center")

# Tree Widget
tv1 = ttk.Treeview(viewing_frame)
tv1.place(relheight=1, relwidth=1)

# Scroll bar creation for the tree widget
tree_scrolly = tkinter.Scrollbar(viewing_frame, orient="vertical", command=tv1.yview)
tree_scrollx = tkinter.Scrollbar(viewing_frame, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=tree_scrollx.set, yscrollcommand=tree_scrolly.set)
tree_scrolly.pack(side="right", fill="y")
tree_scrollx.pack(side="bottom", fill="x")

# Buttons
button1 = tkinter.Button(search_frame, text="Search", command=get_user_stocks)
button1.place(rely=0.3, relx=0.5, relwidth=0.25, relheight=0.05, anchor="e")

button2 = tkinter.Button(
    search_frame, text="Clear Data", command=clear_data
)  # pylint: disable=unnecessary-lambda
button2.place(
    rely=0.3,
    relx=0.5,
    relwidth=0.25,
    relheight=0.05,
    anchor="w",
)

root.mainloop()
