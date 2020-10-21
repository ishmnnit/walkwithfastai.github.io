# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"get_version": "00_utils.ipynb",
         "state_versions": "00_utils.ipynb",
         "create_timm_body": "02_vision.external.timm.ipynb",
         "create_timm_model": "02_vision.external.timm.ipynb",
         "timm_learner": "02_vision.external.timm.ipynb",
         "TabularPandas.export": "03_tab.export.ipynb",
         "load_pandas": "03_tab.export.ipynb",
         "Categorify": "03_tab.stats.ipynb",
         "Normalize.__init__": "03_tab.stats.ipynb",
         "setups": "03_tab.stats.ipynb",
         "FillMissing": "03_tab.stats.ipynb",
         "Recorder.plot_lr_find": "04_lr_finder.ipynb",
         "Learner.lr_find": "04_lr_finder.ipynb"}

modules = ["utils.py",
           "vision/timm.py",
           "tab/export.py",
           "tab/stats.py",
           "callback/lr_find.py"]

doc_url = "https://walkwithfastai.com/"

git_url = "https://github.com/walkwithfastai/walkwithfastai.github.io/tree/master/"

def custom_doc_links(name):
    from nbdev.showdoc import try_external_doc_link
    return try_external_doc_link(name, ['fastcore', 'nbdev', 'fastai', 'timm'])
