<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>GBC Avanta AAS 3D</title>
:root{--bg:#eef1f4;--ink:#1c2630;--card:#fff;--line:#c9d1d9;--acc:#1b6ca8;--hot:#e8662a;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10171d;--ink:#e6edf3;--card:#1a232c;--line:#33414d;--acc:#5aa9e6}}
:root[data-theme="dark"]{--bg:#10171d;--ink:#e6edf3;--card:#1a232c;--line:#33414d;--acc:#5aa9e6}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.4 system-ui,sans-serif}
#cv{height:min(62vh,540px);min-height:320px;position:relative;touch-action:none}
#cv canvas{display:block;width:100%;height:100%}
#hud{position:absolute;left:10px;top:10px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font-size:13px}
#hud b{font-size:18px;color:var(--hot)}
#panel{background:var(--card);border-top:1px solid var(--line);padding:10px}
.row{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
button{font:inherit;font-size:13px;padding:7px 10px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--ink)}
button.on{background:var(--acc);color:#fff;border-color:var(--acc)}
button:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
#info{font-size:13px;min-height:3.6em}
#calc{padding:14px;max-width:980px;margin:0 auto}
#calc h2{font-size:17px;margin:14px 0 8px}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.g label{font-size:12px;display:flex;flex-direction:column;gap:2px}
input,select,textarea{font:inherit;font-size:14px;padding:6px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--ink);width:100%;box-sizing:border-box}
.tw{overflow-x:auto}
.z{display:grid;grid-template-columns:90px 1fr;gap:8px;align-items:end;border:1px solid var(--line);border-radius:8px;padding:8px;margin-bottom:6px}
.z label{font-size:12px;display:flex;flex-direction:column;gap:2px}.z .ck{flex-direction:row;align-items:center;gap:6px;font-size:15px;font-weight:600}
input[type=checkbox]{width:auto;transform:scale(1.3)}
.res{font-size:13px;margin:6px 0;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--card)}
#mg input{width:84px}
[hidden]{display:none!important}
#top{position:sticky;top:0;z-index:5;display:flex;gap:6px;padding:8px 10px;padding-top:calc(8px + env(safe-area-inset-top,0px));background:var(--card);border-bottom:1px solid var(--line)}
#top button{flex:1;font-size:13px;padding:10px 4px}
#home{min-height:min(calc(100vh - 60px),640px);display:flex;align-items:center;justify-content:center;text-align:center;padding:28px 18px;color:#fff;background:linear-gradient(135deg,#17324a,#2c6a8f 55%,#7fb6d1) center/cover no-repeat}
#home h1{font-size:30px;line-height:1.15;margin:0 0 12px;text-shadow:0 2px 8px rgba(0,0,0,.5)}#home p{max-width:560px;margin:0 auto 18px;font-size:15px;text-shadow:0 1px 6px rgba(0,0,0,.6)}
#home .row{justify-content:center}#home button{background:rgba(255,255,255,.16);color:#fff;border-color:rgba(255,255,255,.55);font-size:14px;padding:10px 14px}
.team{list-style:none;padding:0;margin:10px 14px;display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));counter-reset:n}
.team li{counter-increment:n;display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.team li:before{content:counter(n);flex:none;width:30px;height:30px;border-radius:50%;background:var(--acc);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
.team b{display:block}.team span{font-size:13px;opacity:.8}
.sec{margin:12px 14px 4px;font-size:18px}.nt{font-size:12px;margin:4px 14px;opacity:.85}
#calc .nt{margin:6px 0}#calc h2.sec{margin:14px 0 4px}#calc h3{font-size:15px;margin:12px 0 6px}
#calc table input{padding:4px;font-size:13px}.p{margin-top:8px}table{border-collapse:collapse;font-size:13px;width:100%}
th,td{border:1px solid var(--line);padding:4px 8px;text-align:right;white-space:nowrap}th{background:var(--card)}
.bad{color:#c62828;font-weight:600}#cal{margin-top:8px;padding:8px;border:1px solid var(--line);border-radius:8px;background:var(--card)}
#top{overflow-x:auto}#top button{flex:1 0 auto;padding:10px 9px;white-space:nowrap}
#inp,#ik{padding:14px;max-width:980px;margin:0 auto}#inp h3,#ik h3{font-size:15px;margin:14px 0 6px}#ik li{margin:7px 0}#ik li button{margin-left:6px;padding:3px 8px;font-size:12px}#ik p,#ik ul{margin:4px 0}
#rpt{display:none}
@media print{@page{margin:14mm}body>*{display:none!important}body.pr-ik #ik,body.pr-rpt #rpt{display:block!important}
body{background:#fff!important;color:#000!important;font-family:Georgia,"Times New Roman",serif}
#ik{padding:0;max-width:none;font-size:11.5pt;line-height:1.45}#ik h2{font-size:16pt;text-align:center;margin:0 0 8pt}#ik h3{font-size:12.5pt;border-bottom:1px solid #000;padding-bottom:2px;margin:12pt 0 4pt}#ik li{break-inside:avoid}#ik ol,#ik ul{padding-left:18pt}
#rpt{padding:0;font-size:11.5pt;line-height:1.45}#rpt h1{font-size:17pt;text-align:center;margin:0 0 4pt}#rpt .sub{text-align:center;margin:0 0 10pt}#rpt h2{font-size:13pt;border-bottom:1px solid #000;padding-bottom:2px;margin:14pt 0 6pt}
#rpt table{width:100%;border-collapse:collapse;font-size:10.5pt;margin:6pt 0}#rpt th,#rpt td{border:1px solid #000;padding:3px 6px;text-align:center;white-space:normal}#rpt th{background:#e6e6e6}#rpt tr{break-inside:avoid}
#rpt img{display:block;margin:8pt auto;max-width:85%;height:auto;break-inside:avoid}#rpt .eq{margin:6pt 0}}
</style></head><body>
<nav id="top"><button id="n0" class="on">Home</button><button id="n4">Input Data</button><button id="n5">Instruksi Kerja</button><button id="n1">Animasi alat</button><button id="n2">Perhitungan</button><button id="n3">Tentang kami</button></nav>
<section id="home"><div>
<h1>Analisis Kalsium dengan AAS</h1>
<p>Pengaruh gangguan fosfat (PO₄) dan sulfat (SO₄), serta agen pelindung Sr, La, dan EDTA, pada pengukuran Ca dengan GBC Avanta AAS.</p>
<div class="row"><button data-go="4">Input Data</button><button data-go="5">Instruksi Kerja</button><button data-go="1">Animasi alat</button><button data-go="2">Perhitungan</button><button data-go="3">Tentang kami</button></div>
</div></section>
<div id="anim" hidden>
<h2 class="sec">Animasi alat GBC Avanta AAS</h2>
<div id="cv"><div id="hud"><div id="lampinfo"></div></div></div>
<div id="panel">
<div class="row" id="proc"><button id="pv">◀</button><button id="pn" class="on">Mulai prosedur ▶</button><button id="pa">Otomatis</button><button id="pr">Tampilan awal</button></div>
<div class="row" id="wrow" hidden><input type="range" id="wl" min="410" max="435" step="0.1" value="410" style="width:180px"><b id="wlv">410,0</b> nm<button id="wlauto">Scan otomatis</button><button id="wlk">Kunci λ ini</button></div>
<div class="row" id="mrow" hidden><button id="mnx">Larutan berikutnya ▶</button><button id="mrs">Ulangi dari awal</button></div>
<div id="info">Tekan "Mulai prosedur" untuk melihat cara memakai alat langkah demi langkah dengan zoom di tiap langkah. Seret layar untuk memutar 360°, cubit untuk zoom.</div>
<div class="row" id="gasrow"><button id="g1">Asetilen + udara</button><button id="g2" class="on">N₂O + udara</button></div>
<div class="row" id="ctl">
<button id="run" class="on">Jalan</button>
<button id="xray">Tembus pandang</button>
<button id="spin">Putar otomatis</button>
<button id="lidb">Buka tempat lampu</button><button id="manb" class="on">Analis</button>
</div>
<div class="row"><button id="s6">6 slot</button><button id="s8" class="on">8 slot</button><button id="nx">Lampu berikutnya</button></div>
<div class="row" id="parts"></div>

</div>
</div>
<section id="inp" hidden></section>
<section id="ik" hidden>
<div class="row noprint"><button id="ikp">Cetak / simpan PDF</button><button data-go="4">Buka Input Data</button><button data-go="1">Buka animasi alat</button></div>
<h2 class="sec" style="margin-left:0">Instruksi Kerja (IK): Penentuan Kalsium dengan AAS Nyala (GBC Avanta)</h2>
<h3>1. Tujuan dan ruang lingkup</h3><p>Menentukan kadar Ca dalam larutan dengan AAS nyala pada garis 422,7 nm, termasuk menguji gangguan fosfat (PO₄) dan sulfat (SO₄) serta pengaruh pelindung Sr, La, dan EDTA.</p>
<h3>2. Prinsip</h3><p>Atom Ca bebas di dalam nyala menyerap cahaya lampu katoda berongga Ca. Absorbansi (A = log I0/I) sebanding dengan konsentrasi. Persamaan kalibrasi: y = a + bx (y = absorbansi, x = konsentrasi).</p>
<h3>3. Alat dan bahan</h3><ul><li>GBC Avanta AAS, lampu katoda berongga Ca, komputer, exhaust.</li><li>Gas asetilen, N₂O, dan udara dari kompresor.</li><li>Larutan stok Ca, SO₄, PO₄, Sr, La, EDTA; HNO₃ encer untuk pembilas; akuades.</li><li>Labu takar, pipet volumetrik, gelas beaker.</li></ul>
<h3>4. Keselamatan kerja</h3><ul><li>Pakai jas lab, kacamata pengaman, dan sarung tangan.</li><li>Exhaust harus menyala selama nyala hidup. Periksa selang dan sambungan gas dari kebocoran.</li><li>Jangan meninggalkan alat saat nyala hidup. Jauhkan bahan mudah terbakar.</li><li>Darurat: tutup katup tabung gas, matikan alat, dan laporkan ke penanggung jawab lab.</li></ul>
<h3>5. Langkah kerja</h3>
<ol>
<li>Persiapan: nyalakan komputer dan alat, buka gas dan kompresor, hidupkan exhaust.<button class="noprint" data-st="0">Lihat di animasi</button></li>
<li>Pasang lampu katoda berongga Ca pada torret, lalu putar ke jalur cahaya.<button class="noprint" data-st="1">Lihat di animasi</button></li>
<li>Panaskan lampu (warm-up) sampai intensitas stabil.<button class="noprint" data-st="2">Lihat di animasi</button></li>
<li>Atur gas (N₂O + asetilen atau udara + asetilen) dan tekanannya sesuai manual.<button class="noprint" data-st="3">Lihat di animasi</button></li>
<li>Nyalakan nyala dengan igniter. Tunggu stabil, lalu hisap akuades dan lakukan auto-zero.<button class="noprint" data-st="4">Lihat di animasi</button></li>
<li>Siapkan blanko, deret standar Ca, dan larutan uji gangguan. Isi konsentrasinya di menu Input Data.<button class="noprint" data-go="4">Buka Input Data</button></li>
<li>Tentukan panjang gelombang maksimum: hisap standar tertinggi, scan 410–435 nm, lalu kunci λ pada puncak (±422,7 nm).<button class="noprint" data-st="8">Lihat di animasi</button></li>
<li>Ukur blanko, standar (rendah ke tinggi), lalu larutan uji. Bilas kapiler dengan HNO₃ encer dan akuades di antara larutan.<button class="noprint" data-st="9">Lihat di animasi</button></li>
<li>Buat kurva kalibrasi, periksa r, hitung konsentrasi, dan bandingkan absorbansi larutan uji dengan Ca saja.<button class="noprint" data-go="2">Buka Perhitungan</button></li>
<li>Pematian alat: hisap akuades 2–3 menit, tutup katup gas sampai nyala padam, matikan lampu, kompresor, exhaust, lalu komputer.</li>
<li>Bersihkan burner dan peralatan, buang limbah ke wadah yang sesuai, catat data di buku catatan lab.</li>
</ol>
<h3>6. Kriteria penerimaan dan pelaporan</h3><ul><li>Koefisien korelasi kurva kalibrasi r ≥ 0,995.</li><li>Absorbansi sampel berada dalam rentang standar (jika di atas, encerkan).</li><li>Laporkan persamaan regresi, r, konsentrasi Ca, dan persen perubahan sinyal akibat gangguan.</li></ul>
</section>
<section id="calc" hidden>
<h2 class="sec">Perhitungan dan data pengamatan</h2>
<p class="nt">Semua kolom putih bisa diubah. Hasil perhitungan ikut berubah sesuai data yang Anda isi. Boleh memakai koma atau titik desimal.</p>
<div class="row noprint"><button id="rptb">Cetak laporan hasil</button></div><div class="row" id="tabs"></div>
<div class="p" id="p0"></div>
<div class="p" id="p1" hidden></div>
<div class="p" id="p2" hidden></div>
<div class="p" id="p3" hidden></div>
</section>
<section id="about" hidden>
<h2 class="sec">Tentang kami</h2>
<p class="nt" style="margin:4px 14px">Tim penyusun website analisis kalsium dengan AAS.</p>
<ol class="team">
<li><div><b>Arini Khansa Mufidah</b><span>NIM 2560581</span></div></li>
<li><div><b>Fikri Fadhillah</b><span>NIM 2560633</span></div></li>
<li><div><b>Gevan Eirano Yusuf</b><span>NIM 2560635</span></div></li>
<li><div><b>MHD Hasan Zaki</b><span>NIM 2560671</span></div></li>
<li><div><b>Nasywa Arifah Salsa Bila</b><span>NIM 2560712</span></div></li>
<li><div><b>Rikr Rik Lukitasari</b><span>NIM 2560756</span></div></li>
<li><div><b>Siti Azra Alfashahah</b><span>NIM 2560783</span></div></li>
<li><div><b>Siti Rahma Aulia</b><span>NIM 2560787</span></div></li>
<li><div><b>Yasmina Akhmad Intisar</b><span>NIM 2560805</span></div></li>
</ol>
</section>
<div id="rpt"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const $=id=>document.getElementById(id);
const host=$('cv');
const scene=new THREE.Scene();
const cam=new THREE.PerspectiveCamera(45,1,.1,100);
const ren=new THREE.WebGLRenderer({antialias:true,alpha:true});
host.appendChild(ren.domElement);
scene.add(new THREE.HemisphereLight(0xffffff,0x556677,.9));
const dl=new THREE.DirectionalLight(0xffffff,.8);dl.position.set(5,10,6);scene.add(dl);

const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.5,metalness:.2},o));
const parts={};
function add(key,name,desc,mesh){Object.assign(mesh.userData,{key});parts[key]={name,desc,mesh,base:[]};
  mesh.traverse(m=>{if(m.material)parts[key].base.push([m,m.material.emissive?m.material.emissive.getHex():0])});scene.add(mesh);return mesh}

// ===== Bodi bergaya GBC Avanta AAS =====
const shellMat=M(0xf2f3f4,{transparent:true,opacity:1,metalness:.05,roughness:.35});
const bandMat=M(0x3a3a3f,{transparent:true,opacity:1,roughness:.6});
const dark=M(0x14161a,{roughness:.85});
const body=new THREE.Group();
const bxm=(w,h,d,x,y,z,m)=>{const q=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);q.position.set(x,y,z);body.add(q);return q};
bxm(13.6,.25,4.4,.7,.125,0,dark);
const dome=(w,x,par)=>{const c=new THREE.Mesh(new THREE.CylinderGeometry(.6,.6,w,24,1,false,0,Math.PI),shellMat);c.rotation.z=Math.PI/2;c.scale.set(1,1,3.8);c.position.set(x,0,0);par.add(c);return c};
const upper=(w,x)=>{bxm(w,1.2,4.6,x,2.65,0,shellMat);dome(w,x,body).position.y=3.25};
[[8.7,-2.15],[3.9,5.55]].forEach(([w,x])=>{bxm(w,1.1,4.6,x,.8,0,shellMat);bxm(w,.7,4.64,x,1.7,0,bandMat)});
upper(3.9,5.55);upper(.8,-6.1);upper(5.7,-.65);
bxm(2.2,1.2,.1,-4.6,2.65,2.25,shellMat);bxm(2.2,1.2,.1,-4.6,2.65,-2.25,shellMat);
const lid=new THREE.Group();lid.position.set(-4.6,3.25,-2.3);const ld=dome(2.2,0,lid);ld.position.set(0,0,2.3);body.add(lid);
// kompartemen sampel (terbuka di depan)
bxm(1.4,3.0,.2,2.9,1.75,-2.2,dark);bxm(.1,3.0,4.4,2.25,1.75,0,dark);bxm(.1,3.0,4.4,3.55,1.75,0,dark);bxm(1.4,.1,4.4,2.9,3.25,0,dark);bxm(1.4,.1,4.4,2.9,.3,0,dark);
// label, tombol, lampu indikator
const lab=(t,x)=>{const c=document.createElement('canvas');c.width=512;c.height=128;const g=c.getContext('2d');g.fillStyle='#fff';g.font='bold 78px sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText(t,256,68);
  const p=new THREE.Mesh(new THREE.PlaneGeometry(2.6,.65),new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(c),transparent:true}));p.position.set(x,1.7,2.33);body.add(p)};
lab('Avanta AAS',-4.6);lab('GBC',5.9);
[[1.2,1.0,0x1f8a8a],[1.2,.6,0x1f8a8a],[4.6,.8,0xd9b44a],[5.4,.8,0x2e7d32],[6.1,.8,0x1565c0]].forEach(([x,y,c])=>{const k=new THREE.Mesh(new THREE.CylinderGeometry(.13,.13,.08,20),M(c));k.rotation.x=Math.PI/2;k.position.set(x,y,2.33);body.add(k)});
add('body','Rumah alat','Bodi putih bergaya Avanta AAS. Kompartemen hitam di tengah terbuka di depan untuk burner dan ruang semprot, sedangkan optik berada tertutup di kiri dan kanan. Aktifkan "Tembus pandang" untuk melihat bagian dalamnya.',body);

// torret lampu (6 atau 8 slot)
const LAMPS=['Ca','Mg','Na','K','Cu','Zn','Fe','Pb'];
const lamp=new THREE.Group();lamp.position.set(-4.6,2.15,0);
const turret=new THREE.Group();lamp.add(turret);
let nSlot=8,act=0,turT=0,lamp0=null,lampR=.5,instA=1;
add('lamp','Torret lampu katoda berongga','Piringan putar berisi 6 atau 8 lampu. Torret berputar otomatis membawa lampu terpilih ke jalur berkas cahaya. Lampu Ca (422,7 nm) ada di slot 1, lampu lain hanya contoh logam umum.',lamp);
function lampInfo(){const i=((act%nSlot)+nSlot)%nSlot;$('lampinfo').textContent='Lampu aktif: '+LAMPS[i]+' (slot '+(i+1)+'/'+nSlot+')'}
function buildTurret(){
 while(turret.children.length)turret.remove(turret.children[0]);
 const R=.5,r=nSlot==8?.16:.2;
 const disc=new THREE.Mesh(new THREE.CylinderGeometry(R+.3,R+.3,.08,40),M(0x9aa7b2));disc.rotation.z=Math.PI/2;disc.position.x=-.75;turret.add(disc);
 for(let i=0;i<nSlot;i++){const a=i*2*Math.PI/nSlot,ca=i==0,g=new THREE.Group();
  const lb=new THREE.Mesh(new THREE.CylinderGeometry(r,r,1.1,20),M(ca?0xcfd8de:0x8895a0));lb.rotation.z=Math.PI/2;lb.position.x=-.15;
  const lw=new THREE.Mesh(new THREE.CylinderGeometry(r*.65,r*.65,.1,20),M(ca?0x9fd3ff:0x6f8696,{transparent:true,opacity:.85}));lw.rotation.z=Math.PI/2;lw.position.x=.45;
  g.add(lb,lw);g.position.set(0,R*Math.cos(a),R*Math.sin(a));turret.add(g);if(i==0){lamp0=g;lampR=R}}
 act=0;turT=0;turret.rotation.x=0;lampInfo();
 parts.lamp.base=[];lamp.traverse(m=>{if(m.material)parts.lamp.base.push([m,m.material.emissive?m.material.emissive.getHex():0])});
}
buildTurret();
$('s6').onclick=()=>{nSlot=6;$('s6').classList.add('on');$('s8').classList.remove('on');buildTurret()};
$('s8').onclick=()=>{nSlot=8;$('s8').classList.add('on');$('s6').classList.remove('on');buildTurret()};
$('nx').onclick=()=>{act++;turT=-act*2*Math.PI/nSlot;lampInfo()};


// burner + ruang semprot (di dalam kompartemen)
const burner=new THREE.Group();
const bh=new THREE.Mesh(new THREE.BoxGeometry(1.2,.3,.25),M(0x6d7883));bh.position.y=2.15;
const nk=new THREE.Mesh(new THREE.CylinderGeometry(.2,.3,.5,16),M(0x8a96a1));nk.position.y=1.85;
const sc=new THREE.Mesh(new THREE.CylinderGeometry(.5,.4,1.3,24),M(0xcfd8de,{transparent:true,opacity:.7}));sc.position.y=1.0;
const neb=new THREE.Mesh(new THREE.CylinderGeometry(.14,.14,1.5,16),M(0x2f7fb8));neb.rotation.x=Math.PI/2;neb.position.set(0,.9,1.0);
const tube=(pts,c)=>new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts.map(p=>new THREE.Vector3(...p))),24,.04,8),M(c));
burner.add(bh,nk,sc,neb,tube([[.1,1.2,.3],[.5,.9,1.4],[.2,.5,2.0],[-.1,.4,2.2]],0xd32f2f),tube([[-.1,1.2,.3],[-.5,1.0,1.4],[-.2,.55,2.0],[.1,.45,2.2]],0x1565c0));
burner.position.x=2.9;
add('burner','Burner & ruang semprot','Sampel dihisap kapiler, dikabutkan oleh nebulizer bersama oksidan, lalu diselaraskan di ruang semprot. Kabut halus naik ke burner. Nyala N₂O dipakai untuk Ca agar fosfat/sulfat terurai. Selang merah dan biru adalah jalur gas.',burner);
const g1=new THREE.ConeGeometry(.35,1.2,20,1,true);g1.scale(1.6,1,.7);
const g2=new THREE.ConeGeometry(.16,.7,16,1,true);g2.scale(1.6,1,.7);
const flame=new THREE.Mesh(g1,new THREE.MeshBasicMaterial({color:0x3a8dff,transparent:true,opacity:.75,side:2}));flame.position.set(2.9,2.9,0);scene.add(flame);
const core=new THREE.Mesh(g2,new THREE.MeshBasicMaterial({color:0xbfe3ff,transparent:true,opacity:.9,side:2}));core.position.set(2.9,2.65,0);scene.add(core);
parts.burner.flame=[flame,core];
const spark=new THREE.Mesh(new THREE.SphereGeometry(.07,8,8),new THREE.MeshBasicMaterial({color:0xfff59d}));spark.position.set(2.9,2.4,.2);scene.add(spark);

const bkr=new THREE.Group();
bkr.add(new THREE.Mesh(new THREE.CylinderGeometry(.38,.34,.7,24,1,true),M(0xcfe8ff,{transparent:true,opacity:.35,side:2})),new THREE.Mesh(new THREE.CylinderGeometry(.34,.31,.35,24),M(0x7fd0ff,{transparent:true,opacity:.7})),tube([[0,.12,0],[0,.8,-.2],[0,.9,-.8],[0,.9,-1.3]],0xe0e0e0));
bkr.children[0].position.y=.35;bkr.children[1].position.y=.2;bkr.position.set(2.9,0,3.1);scene.add(bkr);
// monokromator
const mono=new THREE.Group();
const mb=new THREE.Mesh(new THREE.BoxGeometry(1.8,1.6,2.2),M(0x7e8c99,
