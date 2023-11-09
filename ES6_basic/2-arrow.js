export default function getNeighborhoodsList() {
	this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

	const self = this;

	let add = (newNeighborhood) => {
	  self.sanFranciscoNeighborhoods.push(newNeighborhood);
	  return self.sanFranciscoNeighborhoods;
	};
	this.addNeighborhood = add;
  }
