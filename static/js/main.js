import { baseProtocol, baseHost } from './configs.js';

const createButton = $('#create-button');
const connectButton = $('#connect-button');

async function connectToRoom() {
    const number = $('#roomNumber').val();
    if (!number || number.length !== 9) {
        return;
    }

    return window.location.href = `${baseProtocol}//${baseHost}/ide/?room=${number}` 
}

async function createOwnRoom() {
    try {
        const request = await fetch(`${baseProtocol}//${baseHost}/api/create_room/`, {method: 'GET'});
        const response = await request.json();

        if (request.ok) {
            const { id, number } = response
            return window.location.href = `${baseProtocol}//${baseHost}/ide/?room=${number}`
        }

    } catch (error) {
        console.error(error.message);
    }

    return;
}

$(document).ready(() => {
    createButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        createOwnRoom();
    });

    connectButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        connectToRoom();
    });

    $('#year').text(new Date().getFullYear());
})