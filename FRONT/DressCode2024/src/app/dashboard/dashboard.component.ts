import { Component } from '@angular/core';
import { RouterLink}  from '@angular/router';
import { DashboardService } from '../services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
  providers:[DashboardService]
})
export class DashboardComponent {

}
