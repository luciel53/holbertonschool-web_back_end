export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
	this._motor = motor;
	this._color = color;
  }

  static get [Symbol.species] () {
    return this;
  }

  cloneCar() {
    const cloneConstr = this.constructor[Symbol.species];
    const clone = new cloneConstr();
    return clone;
  }
}
