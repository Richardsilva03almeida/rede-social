function compartilharTopico() {
    if (navigator.share) {
        navigator.share({
            title: document.title,
            text: 'Veja este tópico no fórum:',
            url: window.location.href
        })
        .then(() => console.log('Compartilhado com sucesso!'))
        .catch((error) => console.log('Erro ao compartilhar:', error));
    } else {
        alert('Compartilhamento não suportado neste dispositivo.');
    }
}