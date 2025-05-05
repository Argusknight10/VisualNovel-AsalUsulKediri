define Prabu_Airlangga = Character('Prabu Airlangga', color="#f1cd73")
define Putri_Dyah = Character('Putri Dyah', color="#4e4225")
define Mpu_Baradha = Character('MPU Baradha', color="#ffffff")

define Marakata = Character('Marakata', color="#eaff00")
define Patih = Character('Patih', color="#7eff2e")

define Anak_Pertama = Character('Anak Pertama', color="#f19073")
define Anak_Kedua = Character('Anak Kedua', color="#f17373")
define Raja_Jenggala = Character('Raja Jenggala', color="#ff5521")
define Raja_Panjalu = Character('Raja Panjalu', color="#ff2121")

label start:
    scene black with fade
    "Abad ke-11. Kerajaan Medang sedang berada di puncak kejayaan. Di bawah pemerintahan Prabu Airlangga, rakyat hidup makmur, ilmu pengetahuan berkembang, dan perdagangan mengalir deras dari pelabuhan ke pelosok desa."
    "Namun, waktu tak pernah bisa dilawan. Usia tua datang membawa keraguan... dan pertanyaan terbesar: Siapa yang pantas mewarisi semua ini?"

    scene istana with fade
    Prabu_Airlangga "Aku telah mendedikasikan hidupku untuk Medang. Kerajaan ini berdiri kokoh karena pengorbanan dan harapan. Tapi kini, saat waktuku hampir habis... kepada siapa semua ini akan kutitipkan?"
    menu:
        "Langkah Sang Prabu":
        "Meminta Pendapat":
            jump minta_pendapat
        "Menentukan Sendiri":
            jump menentukan_sendiri

label minta_pendapat:
        scene dewan with dissolve
        patih "Baginda, para bangsawan dan rakyat sedang menunggu keputusanmu. Tapi izinkan hamba mengingatkan—darah kerajaan masih mengalir pada Dyah, putri Anda."

        Prabu_Pirlangga "Aku tahu itu, Patih. Tapi sejak kecil, Dyah lebih tertarik pada dunia sunyi dan doa. Hatinya tak pernah condong pada kekuasaan..."

        jump tawarkan_tahta

label menentukan_sendiri:
        Prabu_Airlangga "Tak perlu banyak kata. Tahta ini... aku akan tawarkan terlebih dahulu kepada anakku, Dyah. Siapa tahu hatinya berubah."

        jump tawarkan_tahta

label tawarkan_tahta:
        scene taman with dissolve
        Prabu_Airlangga "Anakku, lihatlah langit dan bumi Medang... semua ini bisa menjadi milikmu."

        Putri_Dyah "Ayahanda... sejak lama aku telah memilih jalan yang berbeda. Hatiku tertambat pada kehidupan spiritual. Aku tak sanggup menanggung beban kekuasaan, bukan karena aku takut, tapi karena aku yakin itu bukan jalanku."

        Prabu_Airlangga "Aku menghargai kejujuranmu, Dyah..."

        jump dua_putra

label dua_putra:
        Prabu_Airlangga "Jika bukan Dyah... maka tinggallah dua. Kedua putraku dari selir. Mereka memiliki semangat, tapi juga ambisi. Pilihan ini tak bisa sembarangan..."

        jump misi_bali

label misi_bali:
        Prabu_Airlangga "Mpu Baradha, aku ingin kau pergi ke Bali. Temui saudaraku, Raja Marakata. Lihat bagaimana pemerintahannya berjalan. Mungkin dari sana, aku bisa mendapat inspirasi untuk masa depan Medang."

        menu:
            "Metode Perjalanan":
                "Perahu":
                    jump perahu
                "Terbang":
                    jump terbang

label perahu:
        scene laut_ombak with fade
        "Mpu Baradha menumpang perahu sederhana. Namun di tengah laut, badai datang mendadak. Ombak menggulung tinggi, angin meraung seperti harimau lapar."

        "Saat perahu hampir karam, Mpu Baradha pun berdiri. Dengan tenang ia membaca mantra, dan tubuhnya pun melayang meninggalkan perahu."

        jump tiba_bali

label terbang:
        scene langit_petir with fade
        "Langit menghitam. Petir menyambar berkali-kali. Namun Mpu Baradha tak gentar. Ia menembus badai dengan kesaktiannya, menyusuri langit menuju Bali."

        jump tiba_bali

label tiba_bali:
        scene pura with dissolve
        marakata "Kakanda Airlangga adalah raja besar. Tapi tanah ini sudah kukelola sebaik mungkin."

        Mpu_Baradha "Jika begitu... sudah saatnya Medang dibagi. Bukan karena perpecahan, tapi demi keadilan dan stabilitas."

        jump sungai_pemisah

label sungai_pemisah:
        menu:
            "Sumber Air":
                "Tujuh Mata Air":
                    jump mata_air
                "Awan":
                    jump awan

label mata_air:
        Mpu_Baradha "Aku akan mengambil air dari tujuh mata air suci. Air yang diberkati para leluhur."

        jump brantas

label awan:
        Mpu_Baradha "Langit... berikanlah berkatmu. Aku akan memanggil hujan dari awan-awan paling murni."

        jump brantas

label brantas:
        "Dengan kendi suci, Mpu Baradha menuangkan air ke bumi. Dari tetesannya, mengalir deras sebuah sungai—Brantas. Ia membelah tanah menjadi dua: Panjalu di barat, Jenggala di timur."

        jump persetujuan

label persetujuan:
        menu:
            "Metode Persetujuan":
                "Bimbang":
                    jump bimbang
                "Setuju":
                    jump setuju

label bimbang:
        Anak_Pertama "Aku tak yakin... membagi kerajaan bukan hal kecil."

        Anak_kedua "Tapi mungkin ini cara terbaik untuk menghindari pertumpahan darah."

        jump jabat_tangan

label setuju:
        Anak_Pertama "Jika ini keputusan Ayahanda dan para penasihat... aku akan menerimanya."

        Anak_kedua "Aku pun demikian, Mari kita mulai lembaran baru."

        jump jabat_tangan

label jabat_tangan:
        scene istana with dissolve
        "Dengan tatapan tegas dan hati yang belum sepenuhnya damai, kedua putra Prabu berjabat tangan. Medang pun resmi terbagi."

        jump bertapa

label bertapa:
        scene gua with fade
        "Prabu Airlangga memilih meninggalkan gemerlap istana. Ia menuju pegunungan sunyi, menepi dari dunia fana. Di sanalah ia bertapa... hingga ajal menjemput."

        jump konflik

label konflik:
        "Namun damai hanya bertahan sekejap. Api ambisi mulai menyala. Panjalu dan Jenggala, dua kerajaan muda, mulai saling melirik dengan curiga."

        jump strategi_perang

label strategi_perang:
        menu:
            "Cara Mempersiapkan Perang":
                "Pasukan Seadanya":
                    jump seadanya
                "Mencari Aliansi":
                    jump aliansi

label seadanya:
        "Tanpa banyak waktu, Jenggala mengerahkan pasukan seadanya. Untungnya, desa Turun Hyang berdiri membantu tanpa diminta."

        jump unggul

label aliansi:
        "Panjalu mencoba menjalin aliansi, tapi upaya itu gagal. Sebaliknya, Jenggala mendapat dukungan dari desa Turun Hyang."

        jump unggul

label unggul:
        scene istana_jenggala with dissolve
        Raja_Jenggala "Kemenangan ini bukan milik para bangsawan saja, tapi juga rakyat. Terutama Turun Hyang, desa kecil dengan hati besar."

        "Tahun 1044, desa itu menerima penghargaan dari Jenggala."

        jump pemakaman

label pemakaman:
        menu:
            "Pemakaman":
                "Langsung Lanjut Perang":
                    jump perang_lanjut
                "Tampilkan Proses Pemakaman":
                    jump tampil_pemakaman

label tampil_pemakaman:
        scene gua with fade
        "Jenazah Prabu Airlangga ditemukan di dalam gua sunyi. Ia wafat dalam kesendirian, namun namanya tetap harum di hati rakyat. Tahun 1049 dikenang sebagai tahun kehilangan besar."

        jump perang_lanjut

label perang_lanjut:
    "Perang belum juga usai. Tahun 1052, desa Malenga ikut membantu Jenggala, melawan sekutu Panjalu yang kini bergandengan dengan Kerajaan Tanjung."

    jump anugerah

label anugerah:
    menu:
        "Bentuk Anugerah":
            "Langsung Beri Harta":
                jump langsung_harta
            "Upacara Terlebih Dahulu":
                jump upacara

label langsung_harta:
    "Sebagai tanda terima kasih, Jenggala langsung memberikan harta dan perlindungan pada Malenga."

    jump metode_pemberian

label upacara:
    "Jenggala menggelar upacara penghormatan bagi desa Malenga. Anugerah diberikan setelah prosesi penuh makna."

    jump metode_pemberian

label metode_pemberian:
    menu:
        "Metode Pemberian":
            "Melalui Kepala Desa":
                "Anugerah diberikan secara resmi lewat kepala desa. Ia meneruskan amanat raja dengan penuh tanggung jawab."
            "Langsung ke Rumah":
                "Prajurit kerajaan datang langsung ke rumah-rumah warga. Harta, perlindungan, dan harapan dibawa ke tiap pintu."

    jump akhir

label akhir:
    "Namun sejarah belum berhenti. Tahun 1052, Raja Jenggala tewas dalam serangan mendadak. Kekacauan menyebar. Di tengah porak-poranda, Panjalu muncul sebagai pemenang terakhir."

    "Tapi... apakah benar itu akhir dari segalanya?"

return




