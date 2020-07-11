import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { MainComponent } from './main/main.component';
import { NewsComponent } from './news/news.component';
import { OffersComponent } from './offers/offers.component';
import { DetailsComponent } from './details/details.component';
import { OfferDetailsComponent } from './offer-details/offer-details.component';
import { RequestsComponent } from './requests/requests.component';
import { MapsComponent } from './maps/maps.component';
import { MatRadioModule } from '@angular/material/radio';
import { EmployeeComponent } from './employee/employee.component';
import { AddCompoundComponent } from './add-compound/add-compound.component';
import { AddBlockComponent } from './add-block/add-block.component';
import { AddFlatComponent } from './add-flat/add-flat.component';
import { AddTowerComponent } from './add-tower/add-tower.component';
import { AddShopComponent } from './add-shop/add-shop.component';
import { CompoundControlComponent } from './compound-control/compound-control.component';
import { BlockControlComponent } from './block-control/block-control.component';
import { BlockPipe } from './block.pipe';
import { TowerControlComponent } from './tower-control/tower-control.component';
import { TowerPipe } from './tower.pipe';
import { FlatControlComponent } from './flat-control/flat-control.component';
import { FlatPipe } from './flat.pipe';
import { AddOwnerComponent } from './add-owner/add-owner.component';
import { AddFamilyComponent } from './add-family/add-family.component';
import { OwnerControlComponent } from './owner-control/owner-control.component';
import { RequestControlComponent } from './request-control/request-control.component';
import { OwnerDetailsComponent } from './owner-details/owner-details.component';
import { FamilyPipe } from './family.pipe';
import { FamilyControlComponent } from './family-control/family-control.component';
import { CompoundDetailsComponent } from './compound-details/compound-details.component';
import { BlockDetailsComponent } from './block-details/block-details.component';
import { TowerDetailsComponent } from './tower-details/tower-details.component';
import { FlatStoreDetailsComponent } from './flat-store-details/flat-store-details.component';
import { ShopControlComponent } from './shop-control/shop-control.component';
import { AddOwnershipComponent } from './add-ownership/add-ownership.component';
import { ShopeDetailsComponent } from './shope-details/shope-details.component';
import { OwnershipsPipe } from './ownerships.pipe';
import { AddNewsComponent } from './add-news/add-news.component';
import { AddOfferComponent } from './add-offer/add-offer.component';
import { AddEmployeesComponent } from './add-employees/add-employees.component';
import { EmployeeControlComponent } from './employee-control/employee-control.component';
@NgModule({
  declarations: [
    AppComponent,
    AboutUsComponent,
    MainComponent,
    NewsComponent,
    OffersComponent,
    DetailsComponent,
    OfferDetailsComponent,
    RequestsComponent,
    MapsComponent,
    EmployeeComponent,
    AddCompoundComponent,
    AddBlockComponent,
    AddFlatComponent,
    AddTowerComponent,
    AddShopComponent,
    CompoundControlComponent,
    BlockControlComponent,
    BlockPipe,
    TowerControlComponent,
    TowerPipe,
    FlatControlComponent,
    FlatPipe,
    AddOwnerComponent,
    AddFamilyComponent,
    OwnerControlComponent,
    RequestControlComponent,
    OwnerDetailsComponent,
    FamilyPipe,
    FamilyControlComponent,
    CompoundDetailsComponent,
    BlockDetailsComponent,
    TowerDetailsComponent,
    FlatStoreDetailsComponent,
    ShopControlComponent,
    AddOwnershipComponent,
    ShopeDetailsComponent,
    OwnershipsPipe,
    AddNewsComponent,
    AddOfferComponent,
    AddEmployeesComponent,
    EmployeeControlComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
    FormsModule,
    MatRadioModule,
    RouterModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
