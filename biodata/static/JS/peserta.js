$(document).ready(function () {
    $('#home').attr('href', '/biodata')

    $('#form-title').html("BIODATA PESERTA");
    $('label[for="fullName"]').html('Nama Lengkap');
    $('label[for="dob"]').html('Tanggal Lahir');
    $('label[for="gender"]').html('Jenis Kelamin');
    $('label[for="hp"]').html('Nomor Handphone');
    $('label').append(`<span id='arterisk' class="fs-4">*</span>`);
    $('#gender').prepend(`<option disabled selected value>Pilih jenis kelamin kamu</option>`)

    $('#batal').click(() => {
        $('#mbody1').html('Are you sure want to cancel this?')
        $("#multiFuncModals").modal("show");
    })

    $('#simpan').click( e => {
             
        e.preventDefault();

        // https://www.youtube.com/watch?v=KgnPSmrQrXI
        $.ajax({
            type: "POST",
            url: "peserta/create",
            data: {
                namaLengkap: $('#fullName').val(),
                nik: $('#nik').val(),
                tanggalLahir: $('#dob').val(),
                jenisKelamin: $('#gender').val(),
                nomorHandphone: $('#hp').val(),
                alamat: $('#address').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
           
            success: data => {
                
                if (data.id == 1) {
                    let div =   `<div class="modal-body px-auto" id="modDiv2">
                                    <p class="text-center text-white fw-bolder fs-4" id="mbody2">
                                        <i class="far fa-check-circle fa-lg"></i> ${data.msg}
                                    </p>
                                </div>`;
                    

                    $('#modContResult').html(div);
                    $('#modContResult').attr('style', 'background-color : #068F1C');
                    $("#modalResult").modal("show");
                    $('#modDiv2').click(() => {
                        $('#modInfoResult').addClass('bg-info');
                        $('#mbody3').html(`<i class="fas fa-user-circle fa-lg"></i> Silahkan kunjungi profil Anda untuk mengedit biodata!`)
                        $("#modalInfo").modal("show");
                    })

                } else {
                    let p = `<p class="text-center text-white fw-bolder fs-4" id="mbody2">
                                <i class="far fa-times-circle fa-lg"></i> ${data.msg}
                            </p>`;
                    
                    let div =   `<div class="modal-body px-auto" id="modDiv2" data-bs-dismiss="modal">
                                    ${p}
                                </div>`;

                    $('#modContResult').html(div);
                    $('#modContResult').attr('style', 'background-color : #FF0000');
                    $("#modalResult").modal("show");
                }
            }
        });
    });

});