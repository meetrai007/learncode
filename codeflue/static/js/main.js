document.addEventListener('DOMContentLoaded', function () {
    const subtopicLinks = document.querySelectorAll('.subtopic-link');
    const contentContainer = document.getElementById('content-container');
    const sliderContent = document.querySelector('.slider-content');
    const scrollLeftButton = document.querySelector('.scroll-left');
    const scrollRightButton = document.querySelector('.scroll-right');

    // Highlight the selected subtopic
    function highlightSelectedSubtopic(subtopicId) {
        subtopicLinks.forEach(link => {
            if (link.getAttribute('data-subtopic-id') === subtopicId) {
                link.classList.add('active-subtopic');
            } else {
                link.classList.remove('active-subtopic');
            }
        });
    }

    // Click event on subtopics to show content
    subtopicLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const subtopicId = link.getAttribute('data-subtopic-id');

            // Highlight the selected subtopic
            highlightSelectedSubtopic(subtopicId);

            // Fetch content based on the subtopic ID
            fetch(`/get-content/${subtopicId}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.content) {
                        contentContainer.innerHTML = `
                            <h2>${data.content.title}</h2>
                            <p>${data.content.description}</p>
                            <div>${data.content.english_content}</div>
                            <div>${data.content.hinglish_content}</div>
                        `;
                    }
                });
        });
    });

    // Enable scrolling buttons if the content is overflowed
    if (sliderContent.scrollHeight > sliderContent.clientHeight) {
        scrollLeftButton.style.display = 'block';
        scrollRightButton.style.display = 'block';
    }

    // Scroll left functionality
    scrollLeftButton.addEventListener('click', function () {
        sliderContent.scrollBy({
            top: -200, // Adjust scroll distance vertically
            behavior: 'smooth'
        });
    });

    // Scroll right functionality
    scrollRightButton.addEventListener('click', function () {
        sliderContent.scrollBy({
            top: 200, // Adjust scroll distance vertically
            behavior: 'smooth'
        });
    });
});

