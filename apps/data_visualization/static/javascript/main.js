import 'leaflet/dist/leaflet.js';
import { Map } from './map.js';

let map = new Map();


export function mapOnLoad() {
  map.init();
}
