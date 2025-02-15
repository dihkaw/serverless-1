$(document).ready(function() {
    const apiUrl = 'https://urlAPIgatewayAndaguests'; // Ganti dengan URL API Gateway Anda
    let selectedGuestId = null; // Menyimpan ID tamu yang dipilih untuk diupdate

    // Fetch guests (GET)
    function loadGuests() {
        $.ajax({
            url: apiUrl,
            method: 'GET',
            success: function(data) {
                $('#guestList').empty();
                data.forEach((guest, index) => {
                    $('#guestList').append(`
                        <tr>
                            <td>${index + 1}</td>
                            <td>${guest.name}</td>
                            <td>${guest.message}</td>
                            <td>
                                <button class="btn btn-info btn-sm" onclick="editGuest('${guest.id}', '${guest.name}', '${guest.message}')">Edit</button>
                                <button class="btn btn-danger btn-sm" onclick="deleteGuest('${guest.id}')">Hapus</button>
                            </td>
                        </tr>
                    `);
                });
            }
        });
    }

    // Tambah tamu (POST)
    $('#guestForm').submit(function(event) {
        event.preventDefault();
        const name = $('#name').val();
        const message = $('#message').val();
        const method = selectedGuestId ? 'PUT' : 'POST';
        const url = selectedGuestId ? `${apiUrl}/${selectedGuestId}` : apiUrl;

        $.ajax({
            url: url,
            method: method,
            data: JSON.stringify({ name, message }),
            contentType: 'application/json',
            success: function(response) {
                $('#name').val('');
                $('#message').val('');
                selectedGuestId = null; // Reset selected guest
                loadGuests();
            },
            error: function(error) {
                alert('Terjadi kesalahan. Silakan coba lagi.');
            }
        });
    });

    // Edit guest (PUT)
    window.editGuest = function(id, name, message) {
        selectedGuestId = id;
        $('#name').val(name);
        $('#message').val(message);
    };

    // Hapus guest (DELETE)
    window.deleteGuest = function(id) {
        $.ajax({
            url: `${apiUrl}/${id}`,
            method: 'DELETE',
            success: function() {
                loadGuests();
            },
            error: function(error) {
                alert('Terjadi kesalahan saat menghapus tamu.');
            }
        });
    };

    // Load tamu saat halaman dimuat
    loadGuests();
});
