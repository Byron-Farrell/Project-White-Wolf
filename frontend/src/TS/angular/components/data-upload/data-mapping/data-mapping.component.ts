import { Component, OnInit, AfterViewInit } from '@angular/core';

// --------------- SERVICES ---------------
import { FileUploadService } from '../../../services/file-upload.service';
import { CrimeService } from '../../../services/crime.service';

@Component({
  selector: 'app-data-mapping',
  templateUrl: './data-mapping.component.html',
  styleUrls: ['./data-mapping.component.scss']
})
export class DataMappingComponent implements OnInit, AfterViewInit {

  public columnMappings: any;
  public dataType: string;
  public cities: Array<string>;
  public dropdownStyles: string;
  public cityMappingName: string;
  public cityMapping: any;

  public userCrimeTypes: Array<string>;
  public applicationCrimeTypes: Array<string>;
  public applicationArrestTypes: Array<string>;
  public userArrestTypes: Array<string>;
  public newCity: string;

  private crimeTypeMappingDiv: any;
  private censusBlockMappingDiv: any;
  private censusInformationMappingDiv: any;
  private crimeTypeMappings: any;
  private arrestMappings: any;

  constructor(
    private fileUploadService: FileUploadService,
    private crimeService: CrimeService
  ) { }

  ngOnInit() {
    this.setup();

    if (this.dataType === 'Criminal Data') {
      this.setupCriminalDataMapping();
    }
    else if (this.dataType === 'Census Blocks') {
      this.setupCensusBlockMapping();
    }
    else if (this.dataType === 'Census Information') {
      this.setupCensusInformationMapping();
    }
  }

  ngAfterViewInit() {
    this.crimeTypeMappingDiv = document.getElementById('crimeTypeMapping');
    this.censusBlockMappingDiv = document.getElementById('censusBlockMapping');
    this.censusInformationMappingDiv = document.getElementById('censusInformationMapping');


    if (this.dataType === 'Criminal Data') {
      this.displayCriminalDataMapping();
    }
    else if (this.dataType === 'Census Blocks') {
      this.displayCensusBlockMapping();
    }
    else if (this.dataType === 'Census Information') {
      this.displayCensusInformationMapping();
    }
  }

  private setupCensusInformationMapping(): void {

  }

  private setupCensusBlockMapping(): void {

  }

  private setupCriminalDataMapping(): void {
    this.applicationCrimeTypes = Array();
    this.userCrimeTypes = Array();
    this.crimeTypeMappings = {};

    this.cityMapping = {}

    this.applicationArrestTypes = ['True', 'False'];
    this.userArrestTypes = Array();
    this.arrestMappings = {};


    this.crimeService.loadCrimeTypes()
      .then(json => {
        json.forEach(type => {
          this.applicationCrimeTypes.push(type);
        })
      })
      .catch(error => console.error(error));

    this.fileUploadService.getFileCrimeTypes()
      .then(json => {
        json.forEach(type => {
          this.userCrimeTypes.push(type);
        })
      })
      .catch(error => console.error(error));

      this.fileUploadService.getFileArrestValues()
        .then(json => {
          json.forEach(type => {
            this.userArrestTypes.push(type);
          })
        })
        .catch(error => console.error(error));
  }

  private displayCensusInformationMapping(): void {
    this.crimeTypeMappingDiv.style.display = 'none';
    this.censusBlockMappingDiv.style.display = 'none';
    this.censusInformationMappingDiv.style.display = 'block';
  }

  private displayCensusBlockMapping(): void {
    this.crimeTypeMappingDiv.style.display = 'none';
    this.censusBlockMappingDiv.style.display = 'block';
    this.censusInformationMappingDiv.style.display = 'none';
  }

  private displayCriminalDataMapping(): void {
    this.crimeTypeMappingDiv.style.display = 'block';
    this.censusBlockMappingDiv.style.display = 'none';
    this.censusInformationMappingDiv.style.display = 'none';
  }



  private setup(): void {
    this.columnMappings = this.fileUploadService.getColumnMappings();
    this.dataType = this.fileUploadService.getDataType();

    this.dropdownStyles = 'btn btn-secondary w-100';
    this.cityMappingName = 'City';
    this.cities = Array();

    this.crimeService.loadCities()
      .then(json => {
        json.forEach(type => {
          this.cities.push(type);
        })
      })
      .catch(error => console.error(error));
  }

  public crimeTypeMappingObjectUpdate(userType, type): void {
    this.crimeTypeMappings[userType] = type;
  }

  public ArrestMappingObjectUpdate(userType, type): void {
    this.arrestMappings[userType] = type;
  }

  public cityMappingObjectUpdate(userType, type): void {
    this.cityMapping[userType] = type;
  }

  public import(): void {
    console.log(this.crimeTypeMappings);
  }

  public addCity(): void {
    this.cities.push(this.newCity);
  }
}
