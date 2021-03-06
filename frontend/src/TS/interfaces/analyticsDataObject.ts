interface IsDarkObject {
  yes: number;
  no: number;
}

export interface AnalyticsDataObject {
  isDark: Array<IsDarkObject>;
  isDarkTotal: IsDarkObject;
  timeCrimeCount: any;
}
