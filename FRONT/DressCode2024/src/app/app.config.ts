import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { DashboardService } from './service/dashboard.service';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), DashboardService]
};
