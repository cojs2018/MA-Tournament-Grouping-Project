class Set {
	constructor() { // Empty set type
		this.id = "";
		this.date = new Date();
		this.participants = [];
	}
	
	add(p) {
		try {
			isParticipant = p.ID.length > 0 && && p.Gender.length > 0 && p.Belt.length > 0 && p.Age >= 7 && p.Degree >= -8 && p.Degree <= 8 && p.Height > 0 && p.Weight > 0;
			if(isParticipant) {
				this.paricipants.push(p);
			}
			else {
				throw "Invalid";
			}
		}
		catch(exe) {
			alert("ERROR: Invalid input type!/n/n Input must be object with the following: /n/t # ID /n/t # Gender /n/t # Belt /n/t # Age /n/t # Degree /n/t # Height /n/t # Weight /n/t");
		}
	}
	
	get participants() {
		return this.participants;
	}
	
	indexOf(fn, s=0) { //gets first index of element that meets condition function fn
		return this.participants.indexOf(fn);
	}
	
	lastIndexOf(fn, s=0) { //gets last index of element that meets condition function fn
		return this.participants.lastIndexOf(fn);
	}
	
	remove(i, s=this.participants.length-1) { //removes based on index or last element
		delete this.participants[i];
	}
	
	removeFind(fn) { //removes based on function
		for(int i = 0; i < this.paricipants.length; i++) {
			if(fn(this.participants[i])) {
				delete this.participants[i];
			}
		}
	}		
	
	get id() {
		return this.id;
	}
	
	set id(str) {
		this.id = str;
	}
	
	get date() {
		return this.date();
	}
	
	set date(d) {
		this.date = d;
	}
	
	size() {
		return this.participants.length;
	}
	
}