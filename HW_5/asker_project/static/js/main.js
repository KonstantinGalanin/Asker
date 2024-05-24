function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const init = () => {
    const cards = document.querySelectorAll('.card')

    for(const card of cards) {
        const like_button = card.querySelector('.like-button')
        const like_counter = card.querySelector('.like-counter')
        const question_id = card.dataset.questionId


        like_button.addEventListener('click', () => {
            // const request_url = 'like_question'
            // const curretn_path = window.location.pathname
            // if(curretn_path.includes('question')) {
            //     request_url = 'like_answer'
            // }
            const request = new Request(`/like_question/`, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    question_id: question_id
                })
            })
            fetch(request)
                .then((response) => {
                    if(response.status === 401) {
                        window.location.href = '/login'
                    }
                    else {
                        response.json()
                    }
                })
                .then((data) => like_counter.innerHTML = data.likes_count)
        })
    }



    
}





init()