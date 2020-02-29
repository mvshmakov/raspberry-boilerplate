window.pollSensors = async () => {
    const response = await fetch('/poll_sensors');
    const html = await response.text();

    if (response.ok) {
        document.querySelector('#sensors_placeholder').innerHTML = html;
    } else {
        console.log("HTTP Error: " + response.status + response.statusText);
    }
};

window.pollSensorsManual = async () => {
    const response = await fetch('/poll_sensors_manual');
    const html = await response.text();

    if (response.ok) {
        console.log("Successfully updated!");
        document.querySelector('#manual_sensors_placeholder').innerHTML = html;
    } else {
        console.log("HTTP Error: " + response.status + response.statusText);
    }
};

window.switchButton = async () => {
    const response = await fetch('/switch_button');

    if (response.ok) {
        console.log("Successfully switched!");
    } else {
        console.log("HTTP Error: " + response.status + response.statusText);
    }
};

window.syncAllSensors = async () => {
    const response = await fetch('/sync_all');

    if (response.ok) {
        console.log("Successfully synced!");
    } else {
        console.log("HTTP Error: " + response.status + response.statusText);
    }
};

let intervalID;

window.startUpdates = () => {
    if (intervalID) {
        console.log("Already fetching!")
    } else {
        intervalID = setInterval(window.pollSensors, 2000);
    }
};

window.stopUpdates = () => {
    if (intervalID) {
        clearInterval(intervalID);
        intervalID = null;
    } else {
        console.log("Nothing to stop!");
    }
};

(async () => {
    await Promise.all([window.pollSensors(), window.pollSensorsManual()]);

    window.startUpdates()
})();
