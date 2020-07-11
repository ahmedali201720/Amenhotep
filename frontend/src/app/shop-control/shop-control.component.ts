import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api/api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-shop-control',
  templateUrl: './shop-control.component.html',
  styleUrls: ['./shop-control.component.css'],
})
export class ShopControlComponent implements OnInit {
  shops = [];
  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.onInit();
  }

  onInit(): void {
    this.api.getAllShops().subscribe(
      (data) => {
        this.shops = data;
        console.log(this.shops);
      },
      (error) => {
        console.log(error);
        alert('حدث خطأ ما');
      }
    );
  }

  deleteShop(sid): void {
    this.api.deleteShop(sid).subscribe(
      (data) => {
        this.shops.push(data);
        this.onInit();
      },
      (error) => {
        console.log(error);
        alert('حدث خطا ما');
      }
    );
  }
}
