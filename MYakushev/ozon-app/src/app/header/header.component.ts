import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {AuthLoginData, AuthService} from '../core/auth/auth.service';
import {AuthRegData} from './nav-customer-button/modal-window/pages/modal-page-reg/modal-page-reg.component';
import {ActivatedRoute, Router} from '@angular/router';
import {Subscription} from 'rxjs';
import {ProductService} from '../pages/page-product/services/product.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @Output() onClickSearchButtonBridge: EventEmitter<string> = new EventEmitter<string>();

  private routeSubscription: Subscription;
  private searchTitleSubmit: string;

  constructor(private auth: AuthService, private route: ActivatedRoute, private router: Router, private productService: ProductService) {
  }

  ngOnInit(): void {
    // Проверям залогине ны ли мы
    this.auth.checkLoginStatus();

    // Проверяем, есть ли параметры поиска в url
    this.routeSubscription = this.route.params.subscribe(params => {
      this.searchTitleSubmit = params['search'];
      if (!this.searchTitleSubmit) {
        return;
      }
      this.onClickSearchButtonBridge.emit(this.searchTitleSubmit);
    });
  }

  // Поиск по query параметрам

  searchProducts($event: string) {
    this.router.navigate(['/search', { search: $event }]);
    this.onClickSearchButtonBridge.emit($event);
  }

  // Действия связанные с входом, выходом, регистрацией

  logIn($event: AuthLoginData) {
    this.auth.logIn($event).subscribe();
  }

  logOut() {
    this.auth.logOut().subscribe();
  }

  registration($event: AuthRegData) {
    this.auth.registration($event).subscribe();
  }

}
