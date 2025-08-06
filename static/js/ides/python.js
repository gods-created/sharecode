import { baseProtocol, baseHost, basePort } from '../configs.js';

let socket = null;
const runCodeButton = $('#run-code-button');
const codeInput = $('#code');
const output = $('#output');
let isLocalEdit = false;

async function runCode() {
    const pyodide = await loadPyodide();
    const code = codeInput.val();

    let stdout = '';

    pyodide.setStdout({
        batched: (s) => { stdout += `${s}\n`; },
    });
    pyodide.setStderr({
        batched: (s) => { stdout += `${s}\n`; },
    });

    output.text('');
    
    try {
      const result = await pyodide.runPythonAsync(code);
      send(
        stdout || (result !== undefined ? result.toString() : 'Done.'), 
        'output'
      );
    } catch (e) {
      output.text(e);
    }
  }

function send(value, block) {
    const data = { 'value': value, 'block': block };

    if (socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify(data));
    } else if (socket.readyState === WebSocket.CONNECTING) {
        socket.addEventListener('open', function onOpen() {
            socket.send(JSON.stringify(data));
            socket.removeEventListener('open', onOpen);
        });
    } else {
        console.error('WebSocket is not open. State:', socket.readyState);
    }
}

function receive() {
    socket.addEventListener('message', (ev) => {
        const { value, block, type } = JSON.parse(ev.data);
        if (block === 'codeInput') {
            if (!isLocalEdit && value !== codeInput.val()) {
                codeInput.val(value);
            }

            isLocalEdit = false;
        } else if (block === 'output' && value !== output.text()) {
            output.text(value);
        }
    });
}

async function room_content(room_number) {
    try {
        const request = await fetch(`${baseProtocol}//${baseHost}/api/room_content/`, {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ room_number })
        });

        const response = await request.json();

        if (request.ok) {
            response.code ? codeInput.val(response.code) : false;
            response.output ? output.text(response.output) : false;
        }

    } catch (error) {
        console.error(error.message);
    }
}

$(document).ready(async () => {
    const number = $('#room-number').text();
    // const port = Number(basePort) + 1;
    // const host = baseHost.replaceAll(basePort, port);
    socket = new WebSocket(`ws://${baseHost}/ws/code/${number}/`);

    codeInput.on('keydown', (ev) => {
        if (ev.key === 'Tab') {
            ev.preventDefault();
            const textarea = ev.target;
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            textarea.value = textarea.value.substring(0, start) + '\t' + textarea.value.substring(end);
            textarea.selectionStart = textarea.selectionEnd = start + 1;
        }
    })

    codeInput.on('input', (ev) => {
        ev.preventDefault();
        isLocalEdit = true;
        send(codeInput.val(), 'codeInput'); 
    });

    runCodeButton.off('click').on('click', async (ev) => {
        ev.preventDefault();
        await runCode();
    });

    receive();
    await room_content(number);
});