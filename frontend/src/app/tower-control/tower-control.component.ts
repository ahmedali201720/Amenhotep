import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api/api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-tower-control',
  templateUrl: './tower-control.component.html',
  styleUrls: ['./tower-control.component.css'],
})
export class TowerControlComponent implements OnInit {
  towers = [];
  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.onInit();
  }

  onInit(): void {
    this.api.getAllTowers().subscribe(
      (data) => {
        this.towers = data;
      },
      (error) => {
        console.log(error);
        alert('حدث خطأ ما');
      }
    );
  }

  deleteTower(tid): void {
    this.api.deleteTower(tid).subscribe(
      (data) => {
        this.towers.push(data);
        this.onInit();
      },
      (error) => {
        console.log(error);
        alert('حدث خطا ما');
      }
    );
  }
}
