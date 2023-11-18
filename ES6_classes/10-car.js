export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const CloneConstr = this.constructor[Symbol.species];
    const clone = new CloneConstr();
    return clone;
  }
}
