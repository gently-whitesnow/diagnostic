using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;

namespace Service.Cases;

public static class SimpleAsyncApiHandler
{
    public static async Task HandleAsync(HttpContext context)
    {
        var httpClient = new HttpClient();

        var response = await httpClient.GetStringAsync("https://example.com");
        await context.Response.WriteAsync(response);
    }
}