#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Code illustration: 2.03

Adding View Menu Items to demonstrate
other Types of Menu Items
    1. Checkbutton menu-item
    2. Radiobutton menu-item
    3. Cascade menu-item

@Tkinter GUI Application Development Blueprints
"""

def main():

    import tkinter as tk

    root = tk.Tk()
    root.geometry('350x350')
    BLANK_SPACE = " "  # One empty space
    PROGRAM_NAME = " Footprint Editor "
    root.title(20 * BLANK_SPACE + PROGRAM_NAME)

    # getting icons ready for compound menu
    new_file_icon = tk.PhotoImage(file='icons/new_file.gif')
    open_file_icon = tk.PhotoImage(file='icons/open_file.gif')
    save_file_icon = tk.PhotoImage(file='icons/save.gif')
    cut_icon = tk.PhotoImage(file='icons/cut.gif')
    copy_icon = tk.PhotoImage(file='icons/copy.gif')
    paste_icon = tk.PhotoImage(file='icons/paste.gif')
    undo_icon = tk.PhotoImage(file='icons/undo.gif')
    redo_icon = tk.PhotoImage(file='icons/redo.gif')

    # Adding Menubar in the widget

    menu_bar = tk.Menu(root)        # menu begins

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    # all file menu-items will be added here next
    file_menu.add_command(label="New", accelerator='Ctrl+N',
                          compound="left", image=new_file_icon, underline=0)
    file_menu.add_command(label="Open", accelerator="Ctrl+O",
                          compound="left", image=open_file_icon, underline=0)
    file_menu.add_command(label="Save", accelerator="Ctrl+S",
                          compound="left", image=save_file_icon)
    file_menu.add_command(label="Save as", accelerator="Shift+Ctrl+S")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", accelerator="Alt+F4")

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Undo", accelerator="Ctrl+Z",
                          compound="left", image=undo_icon)
    edit_menu.add_command(label="Redo", accelerator="Ctrl+Y",
                          compound="left", image=redo_icon)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", accelerator="Ctrl+X",
                          compound="left", image=cut_icon)
    edit_menu.add_command(label="Copy", accelerator="Ctrl+C",
                          compound="left", image=copy_icon)
    edit_menu.add_command(label="Paste", accelerator="Ctrl+V",
                          compound="left", image=paste_icon)
    edit_menu.add_separator()
    edit_menu.add_command(label="Find", underline=0, accelerator="Ctrl+F")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", underline=7, accelerator="Ctrl+A")

    ##
    # Implementing Checkbutton, Radiobutton and Cascade menu-items under View Menu in this iteration
    ##

    view_menu = tk.Menu(menu_bar, tearoff=0)
    # View menu-items displays some variations,
    # so we tackle view menu code to be entered here in a later section
    menu_bar.add_cascade(label="View", menu=view_menu)
    show_line_number = tk.IntVar()
    show_line_number.set(1)
    view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
    show_cursor_info = tk.IntVar()
    show_cursor_info.set(1)
    view_menu.add_checkbutton(label="Show Cursor Location at Bottom", variable=show_cursor_info)
    highligth_line = tk.IntVar()
    view_menu.add_checkbutton(label="HighLight Current Line", onvalue=1,
                              offvalue=0, variable=highligth_line)
    themes_menu = tk.Menu(menu_bar, tearoff=0)
    view_menu.add_cascade(label="Themes", menu=themes_menu)

    """
    color scheme is defined with dictionary elements like -
            theme_name : foreground_color.background_color
    """
    color_schemes = {
        'Default': '#000000.#FFFFFF',
        'Greygarious': '#83406A.#D1D4D1',
        'Aquamarine': '#5B8340.#D1E7E0',
        'Bold Beige': '#4B4620.#FFF0E1',
        'Cobalt Blue': '#ffffBB.#3333aa',
        'Olive Green': '#D1E7E0.#5B8340',
        'Night Mode': '#FFFFFF.#000000',
    }

    theme_choice = tk.StringVar()
    theme_choice.set('Default')
    for k in sorted(color_schemes):
        themes_menu.add_radiobutton(label=k, variable=theme_choice)








    about_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="About")
    about_menu.add_command(label="Help")

    root.config(menu=menu_bar)          # menu ends

    # add top shortcut bar & left line number bar
    shortcut_bar = tk.Frame(root, height=25, background='light sea green')
    shortcut_bar.pack(expand="no", fill="x")

    line_number_bar = tk.Text(root, width=4, padx=3, takefocus=0, border=0,
                              background='khaki', state="disabled", wrap="none")
    line_number_bar.pack(side="left", fill="y")

    # add the main content Text widget and Scrollbar widget
    content_text = tk.Text(root, wrap="word")
    content_text.pack(expand="yes", fill="both")
    scroll_bar = tk.Scrollbar(content_text)
    content_text.configure(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=content_text.yview)
    scroll_bar.pack(side="right", fill="y")

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
