let i = 0;

function loadDynamicImage() {
    document.getElementById('dynamicImage').src = `images/image-${i}.jpg`;
    i++;
}

loadDynamicImage();

setInterval(loadDynamicImage, 3000);

const getStartedButton = document.getElementById('getStartedButton');
const mainContent = document.getElementById('mainContent');

getStartedButton.addEventListener('click', function() {
    mainContent.style.display = 'block';
    getStartedButton.style.display = 'none';
});
