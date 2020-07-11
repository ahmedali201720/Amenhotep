import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api/api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-flat-control',
  templateUrl: './flat-control.component.html',
  styleUrls: ['./flat-control.component.css'],
})
export class FlatControlComponent implements OnInit {
  flats = [];
  cid: number;
  bid: number;
  tid: number;
  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.onInit();
  }

  onInit(): void {
    this.api.getAllFlats().subscribe(
      (data) => {
        this.flats = data;
      },
      (error) => {
        console.log(error);
        alert('حدث خطأ ما');
      }
    );
  }

  deleteFlat(fid): void {
    this.api.deleteFlat(fid).subscribe(
      (data) => {
        this.flats.push(data);
        this.onInit();
      },
      (error) => {
        console.log(error);
        alert('حدث خطا ما');
      }
    );
  }
}
