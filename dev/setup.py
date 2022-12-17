import sys
from cx_Freeze import setup, Executable

company_name="E. Bradfield"
product_name="Helen's Helper"

bdist_msi_options = {
    'upgrade_code':'{2047HELENSHELPER17122022}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
}

build_exe_options = {
    'includes':['spacy', 'openai']
}

base = None
if sys.platform=='win32':
    base='Win32GUI'
    
exe = Executable(script='app.py', base=base)

setup(
    name=product_name,
    version='1.0.0',
    description='minecraft mod advisor',
    executables=[exe],
    options={'bdist_msi':bdist_msi_options, 'build_exe':build_exe_options}
)