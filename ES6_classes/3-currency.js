export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    const val = this._code = value;
    return val;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    const val = this._name = value;
    return val;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
