let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        let product_id = this.dataset.product
        let action = this.dataset.action
        console.log('productID:', product_id, 'action:', action)

        console.log('user:', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        }else {
            updateUserOrder(product_id, action)
        }
    }) 
}
function updateUserOrder(product_id, action) {
    console.log('Welcome you are a legend and sending data...')
    
    let url = 'update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'product_id': product_id, 'action': action})
    })
    .then((response) => {
        return response.json()
    })  
    .then((data) => {
        console.log('data:', data)
    })
}