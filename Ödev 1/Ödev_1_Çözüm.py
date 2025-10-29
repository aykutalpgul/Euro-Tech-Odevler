"""ÖDEV: Virtual Environment Adımları
=================================

1) Virtual environment oluşturma (venv örneği):
   python -m venv aykut_env 

2) Environment aktif etme:
   Windows: .\aykut_env\Scripts\activate
   Linux/Mac: source aykut_env/bin/activate

3) Yüklü paketleri listeleme:
   pip list 

4) NumPy (güncel) + Pandas==1.2.1 yükleme:
   pip install numpy pandas==1.2.1

5) NumPy versiyonu öğrenme:
   python -c "import numpy as np; print(np.__version__)"

6) Pandas upgrade + versiyon öğrenme:
   pip install --upgrade pandas
   python -c "import pandas as pd; print(pd.__version__)"

7) NumPy silme:
   pip uninstall numpy

8) seaborn + matplotlib yükleme:
   pip install seaborn matplotlib

9) Paketleri YAML olarak export etme:
   venv:   pip freeze > environment.yaml
   conda:  conda env export > environment.yaml

10) Environment silme:
   venv:   deactivate  ardından klasörü sil (rm -rf aykut_env veya rmdir /s /q aykut_env)
   conda:  conda deactivate  ardından conda env remove -n aykut_env

Not: Tüm bu komutlar terminalde (CMD, PowerShell, ya da Linux/Mac Terminal) çalıştırılır.
 """