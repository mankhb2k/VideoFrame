# Cấu trúc một dự án video

```
Videos/<yyyy-mm-ten>/
├── kich-ban/           script.md, loi-thoai/canhN_*.txt, bang-phat-am.csv
├── video/              dự án HyperFrames (index.html, BRIEF.md, STORYBOARD.md, design.md)
│   ├── compositions/frames/NN-ten.html  (+ .sfx.json, .motion.json)
│   └── assets/         audio/ (wav, words-*.json, moc-canh.json, sfx-track.wav), images/, sfx/, fonts/
├── renders/            draft-30fps.mp4, final-60fps.mp4   (không đưa lên git)
├── thumbnail/
└── dang-bai/           tieu-de.md, mo-ta.md, tags.txt
```

Quy ước: tên file không dấu; mỗi class/id trong cảnh có tiền tố `sN-`; khai báo `@font-face` trong `index.html` và trong từng file cảnh;
dừng `hyperframes preview` trước khi sửa file bằng tay (Studio tự thêm thuộc tính vào HTML).
