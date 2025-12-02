
class HeadBase extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({mode: 'open'})
        const template = document.getElementById('headbase').contentEditable.cloneNode(true);
        shadowRoot.appendChild(template);
    }
}

class NavBase extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({mode: 'open'})
        const template = document.getElementById('navbase').contentEditable.cloneNode(true);
        shadowRoot.appendChild(template);
    }
}


customElements.define("headbase", ExtendBase);
customElements.define("navbase", ExtendBase);