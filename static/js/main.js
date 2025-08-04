import { baseProtocol, baseHost } from './configs.js';

const createButton = $('#create-button');
const connectButton = $('#connect-button');
const language = $('#language');
const alert = $('#alert');
const alertCloseButton = alert.find('.btn-close');

function showOrHideAlert(message=null) {
    if (message) {
        const textBlock = alert.find('strong');
        textBlock.text(message)
    }
    
    alert.addClass('d-block').removeClass('d-none');
}

async function connectToRoom() {
    const number = $('#roomNumber').val();
    if (!number || number.length !== 9) {
        return;
    }

    return window.location.href = `${baseProtocol}//${baseHost}/ide/?room=${number}` 
}

async function createOwnRoom(language) {
    let error = null;

    try {
        const request = await fetch(`${baseProtocol}//${baseHost}/api/create_room/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ language })
        });
        const response = await request.json();
        
        if (request.ok) {
            const { id, number } = response
            return window.location.href = `${baseProtocol}//${baseHost}/ide/?room=${number}`
        } else {
            const keys = Object.keys(response);
            const value = response[keys[0]];
            error = Array.isArray(value) ? value[0] : value;
        }

    } catch (err) {
        error = err.message;
    }

    showOrHideAlert(error);
}

$(document).ready(() => {
    createButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        createOwnRoom(language.val());
    });

    connectButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        connectToRoom();
    });

    alertCloseButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        if (alert.hasClass('d-block')) {
            alert.toggleClass('d-none d-block');
        }
    });

    $('#year').text(new Date().getFullYear());
})