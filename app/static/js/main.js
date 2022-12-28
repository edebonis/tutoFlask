const getTitleFromCategory = category => {
    const titles = {
        'success': 'Bien hecho',
        'warning': 'Atención',
        'info': 'Atención',
        'error': 'Ooops...'
    }
    return titles[category]
}

function showMessageAlert(category, message) {
    Swal.fire({
  icon: category,
  title: getTitleFromCategory(category),
  text: message,
})
}