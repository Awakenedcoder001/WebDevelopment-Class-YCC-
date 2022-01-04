class food {
    constructor (name, did, batch, nationality,nationallanguage)
    {
        this.name=name; 
        this.did=did; 
        this.batch=batch;
        this.nationality=nationality;
        this.nationallanguage= nationallanguage;

    }
    display(){
        console.log
    }
    static display(){
        console.log(`name=${this.name},did=${this.did}, batch=${this.batch}, nationality="${this.nationality}, nationallanguage="${this.nationallanguage};`)
    }

}

