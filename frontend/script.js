document.getElementById('contentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const topic = document.getElementById('topic').value;
    const file = document.getElementById('file').files[0];

    alert('Đã nhận chủ đề: ' + topic + '\nFile: ' + (file ? file.name : 'Không có'));

    // Giả lập phản hồi từ AI
    document.getElementById('aiContent').value = `Bài viết mẫu về chủ đề: ${topic}\n... (AI sẽ tạo nội dung ở đây)`;
});

document.getElementById('saveBtn').addEventListener('click', function() {
    alert('Đã lưu chỉnh sửa! AI sẽ học từ nội dung bạn chỉnh sửa.');
});
