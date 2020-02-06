// --------------- ANGULAR ---------------
import { Component, OnInit } from '@angular/core';

// -------------- INTERFACES --------------
import { FilterOptionsObject } from '../../../interfaces/filterOptionsObject'

// --------------- SERVICES ---------------
import { CrimeService } from '../../services/crime.service';

@Component({
  selector: 'app-map-selector',
  templateUrl: './map-selector.component.html',
  styleUrls: ['./map-selector.component.scss']
})
export class MapSelectorComponent implements OnInit {

  genericSelectedFilterOptions: FilterOptionsObject;;

  constructor(private crimeService: CrimeService) {

  }

  ngOnInit() {

  }


  private loadData(): void {
    let loading = this.crimeService.loadCrimeData(this.genericSelectedFilterOptions);

    loading.then(x => console.log(x))
  }

  onSelect(): void {
    this.loadData();
  }

  genericSelectedFiltersChanged(selectedFilters: FilterOptionsObject): void {
    this.genericSelectedFilterOptions = selectedFilters;
  }
}