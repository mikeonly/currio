`magneuropy` folder is a module that can be installed with `pip` in editable mode. This allows you to make changes to the code and have them reflected in the installed module without having to reinstall it. 

Run this from the `magneuropy` folder to install the module in editable mode:

`pip install --no-build-isolation --no-deps -e .`

After that, in the current python environment, you can import the module with `import magneuropy` and use its functions with `magneuropy.function_name()` everywhere! 