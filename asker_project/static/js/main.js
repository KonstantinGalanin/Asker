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
    const cards = document.querySelectorAll('.question-card')
    for(const card of cards) {
        console.log(1)
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
                        return response.json()
                    }
                })
                .then((data) => like_counter.innerHTML = data.likes_count)
        })
    }


    const answer_cards = document.querySelectorAll('.answer-card')
    for(const card of answer_cards) {
        
        const like_button = card.querySelector('.like-button')
        const like_counter = card.querySelector('.like-counter')
        const answer_id = card.dataset.answerId

        like_button.addEventListener('click', () => {
            const request = new Request(`/like_answer/`, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    answer_id: answer_id
                })
            })
            fetch(request)
                .then((response) => {
                    if(response.status === 401) {
                        window.location.href = '/login'
                    }
                    else {
                        return response.json()
                    }
                })
                .then((data) => like_counter.innerHTML = data.likes_count)
        })
    }


    const right_labels = document.querySelectorAll('.form-check-input')
    for(const label of right_labels) {

        label.addEventListener('click', () => {
            const question_id = label.dataset.questionId
            const answer_id = label.dataset.answerId
            console.log(question_id)

            const request = new Request(`/right_answer/`, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    question_id: question_id,
                    answer_id: answer_id
                })
            })
            fetch(request)
                .then((response) => {
                    if(response.status === 401) {
                        window.location.href = '/login'
                    }
                    else {
                        return response.json()
                    }
                })
                .then((data) => label.checked = data.right_answer)
            })
    }
}





init()