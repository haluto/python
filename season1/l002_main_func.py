print __name__

#This is a comment line.

'''

This is a comment paragraph.

Some comments here:
1. filename: 
    1) Start with alphabet instead of number;
    2) Use "_" instead of "-"

Why?
Because:

2. A python file can also be a python module.
    You can "import l002_main_func" in other python scripts, 
    but module name cannot be started with number and cannot be with "-".

3. About __name__
    1) When you run the script directly: 
        $ python l002_main_func.py
        __name__ would be '__main__'
    2) When you import it as a module:
        >>> import l002_main_func
        __name__ would be file/module name, "l002_main_func"

So,

4. Use main function for business code.
    if __name__ == '__main__':
        main()
Then the main() function won't be executed if imported by others.

'''
