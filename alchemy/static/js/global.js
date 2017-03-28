/**
 * Script global
 *
 * Author: Khairul Anwar <htpp://iruwl.github.io>
 * Date  : 20161014
 */
console.log(`%c  ____ ____ ____ ____ ____ ____ ____ ____ ____
 ||O |||p |||e |||n |||S |||I |||P |||K |||D ||
 ||__|||__|||__|||__|||__|||__|||__|||__|||__||
 |/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|

Ini merupakan  fitur dari browser yang ditujukan
untuk   pengembang   aplikasi.  Jika  Anda  atau
seseorang menyarankan Anda untuk  mengcopy-paste
sesuatu disini untuk mengaktifkan fitur aplikasi
atau menghack aplikasi maka itu merupakan sebuah
pelanggaran. Aplikasi ini dilindungi  Hak Cipta.`, "color:blue;font-family:monospace;");
console.log("%cecho%cirul.", "color:red", "color:black");
/** Simpan state sidebar */
if (Boolean(sessionStorage.getItem("sidebar-toggle-collapsed"))) {
    $("body").addClass('sidebar-collapse')
        // console.log('sidebar-collapse=add');
}
$('.sidebar-toggle').click(function() {
    // event.preventDefault();
    if (Boolean(sessionStorage.getItem("sidebar-toggle-collapsed"))) {
        sessionStorage.setItem("sidebar-toggle-collapsed", "");
        // console.log('sidebar-collapse=false');
    } else {
        sessionStorage.setItem("sidebar-toggle-collapsed", "1");
        // console.log('sidebar-collapse=true');
    }
});
/** Disable form submit when key 13 (enter/return key) pressed */
$(document).keypress(function(event) {
    if (event.which == '13') {
        event.preventDefault();
    }
});
/** Focus on first element */
$(document).ready(function() {
    $('input:visible:enabled:first').focus();
});
/** Disable direct editing, biasanya disanding dengan input yang harus dipilih menggunakan picker */
$('.no_edit').on('keypress', function(e) {
    e.preventDefault();
});
/** Select all text pada kolom input (class form-control) ketika diklik */
$('.form-control').on("click", function() {
    $(this).select();
});
/** Animasi ajax loading */
$(document).ajaxSend(function() {
    $('.loading').fadeIn(500);
});
$(document).ajaxComplete(function() {
    $('.loading').fadeOut(500);
});
/** act: kembali ke home/beranda */
$('.back-home').click(function() {
    window.location = getModuleUrl();
});
/** act: kembali ke list controller */
$('.back-parent-controller').click(function() {
    window.location = getControllerUrl();
});
/** act: menghandle proses ajax */
function ajaxHandler(url, data, type = 'POST') {
    return $.ajax({
        url: url,
        data: data,
        type: type,
        dataType: "json",
        success: function(j) {
            // atur sendiri aja, mo tampil alert ato tidak, karena digunakan rame2
            // alert(j.message)
        },
        error: function(xhr, type, exception) {
            alert("Ajax error response !" + "\nStatus : " + xhr.status + "\nMessage : " + xhr.statusText + "\nBody :\n" + xhr.responseText);
        }
    });
};
/** Kembali ke atas halaman */
function scrollTop() {
    $('html,body').scrollTop(0);
}
/** Fungsi untuk mendapatkagetBaseUrln url base */
function getBaseUrl(segment) {
    if (segment) {
        return bsUrl + segment;
    } else {
        return bsUrl;
    }
};
/** Fungsi untuk mendapatkan url site */
function getSiteUrl(segment) {
    if (segment) {
        return stUrl + segment;
    } else {
        return stUrl;
    }
};
/** Fungsi untuk mendapatkan url dari modul yang aktif */
function getModuleUrl(segment) {
    if (segment) {
        return mdUrl + segment;
    } else {
        return mdUrl;
    }
};
/** Fungsi untuk mendapatkan url dari modul yang aktif beserta dengan segmen controllernya */
function getControllerUrl(segment) {
    if (segment) {
        return ctUrl + segment;
    } else {
        return ctUrl;
    }
};
/**
 * move focus on next field when enter is pressed
 * @link: http://stackoverflow.com/questions/24209588/how-to-move-focus-on-next-field-when-enter-is-pressed
// 1. register jQuery extension
jQuery.extend(jQuery.expr[':'], {
    focusable: function(el, index, selector) {
        return $(el).is('a, button, :input, [tabindex]');
        return $(el).is(':input, [tabindex]');
    }
});
// 2. bind to act
$(document).on('keydown', 'input,select', function(e) {
    if (e.which == 13) {
        e.preventDefault();
        // console.log('next focus');

        // Get all focusable elements on the page
        var $canfocus = $(':focusable');
        var index = $canfocus.index(document.activeElement) + 1;
        if (index >= $canfocus.length) index = 0;
        $canfocus.eq(index).focus();
    }
});
 */