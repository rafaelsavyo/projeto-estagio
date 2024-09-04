function carregar () {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var minutos = data.getMinutes()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas e ${minutos} minutos.`
    if (hora >= 0 && hora < 12) {
        // BOM DIA !
        img.src = 'manha.png'
        document.body.style.background = '#dabfa2'
    } else if (hora >= 12 && hora < 18) {
        // BOA TARDE !
        img.src = 'tarde.png'
        document.body.style.background = '#7f7f83'
    } else {
        // BOA NOITE !
        img.src = 'noite.png'
        document.body.style.background = '#463557'
    }
}