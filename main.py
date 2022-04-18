#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

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

    view_menu = tk.Menu(menu_bar, tearoff=0)
    # View menu-items displays some variations,
    # so we tackle view menu code to be entered here in a later section
    menu_bar.add_cascade(label="View", menu=view_menu)

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
