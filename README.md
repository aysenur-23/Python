# Python


Python programlama dilinin temelleri başlıklar altında incelenmiştir. 
Yazılan yorum satıları konuyu anlatır niteliktedir.

*Sanal Ortam Kullanımı*

- Sanal ortamları listeleme: conda env list
- Sanal ortam oluşturma: conda create -n myenv(isim)
- Sanal ortamı aktifleştirme: conda activate myenv
- Sanal ortamı pasifleştirme: conda deactivate
- Ortam içerisinde yüklü paketleri görme: conda list
- paket yükleyici, son versiyonu: conda install numpy
- birden fazla paketi aynı anda yükleme: conda install pandas scipy
- belirli bir versiyonu yükleme: conda install numpy=1.20.1
- paketi silme: conda remove numpy
- paket yükseltme: conda upgrade numpy
- tüm kütüphaneleri güncelle: conda upgrade -all
- kullanılan paketleri göndermek için: conda env export > environent.yaml
- environment silme : conda env remove -n myenv
- paketleri toplu olarak kurma: conda env create -f environment.yaml

- pip : pypi (python package index)
- paket yükleme: pip install pandas
- versiyona göre paket yükle: pip install pandas==1.2.1
- kullanılan paketleri göndermek için: pip
