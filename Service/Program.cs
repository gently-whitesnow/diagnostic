using Microsoft.AspNetCore.Builder;
using Service.Cases;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/simple-api", SimpleAsyncApiHandler.HandleAsync);
app.MapGet("/simple", ()=>"hello");

app.Run();